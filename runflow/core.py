"""Core module for runflow."""

import enum
import inspect
import logging
import traceback
import asyncio
from functools import reduce

import networkx
from decouple import config
from tenacity import (
    after_log,
    retry,
    stop_after_delay,
    stop_after_attempt,
)

from . import hcl2, utils
from .errors import (
    RunflowAcyclicTasksError,
    RunflowSyntaxError,
)
from .hcl2_parser import LarkError
from .registry import get_task_class, register_task_class
from .utils import import_module

logger = logging.getLogger(__name__)


DEPENDS_ON_KEY = "_depends_on"


class TaskStatus(enum.Enum):
    """Task execution status."""

    PENDING = enum.auto()
    SUCCESS = enum.auto()
    FAILED = enum.auto()
    CANCELED = enum.auto()


class TaskResult:
    """Task execution result."""

    def __init__(self, status):
        self.status = status
        self._result = None
        self._exception = None

    @property
    def result(self):
        """Get task result."""
        if self._exception:
            raise ValueError(
                "Task has no result due to a failed run."
            ) from self._exception
        return self._result

    @result.setter
    def result(self, _result):
        """Set task result."""
        self.status = TaskStatus.SUCCESS
        self._result = _result

    @property
    def exception(self):
        """Get task exception."""
        if self._result:
            raise ValueError("Task has no exception due to a successful run.")
        return self._exception

    @exception.setter
    def exception(self, _exception):
        """Set task exception."""
        self.status = TaskStatus.FAILED
        self._exception = _exception


class Task:
    """Task object maintains the running status."""

    def __init__(self, type, runner, name, payload):
        self.type = type
        self.runner = runner
        self.name = name
        self.payload = payload
        self.namespace = ""

    def __repr__(self):
        return (
            f"Task(type={self.type}, "
            f"name={self.name}, "
            f"payload={self.payload})"
        )

    def __str__(self):
        return (
            f"{self.namespace}{self.namespace and ' > ' or ''}"
            f"task.{self.type}.{self.name}"
        )

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, o):
        return self.type == o.type and self.name == o.name

    def set_namespace(self, namespace):
        self.namespace = namespace

    def should_run(self, context):
        return all(
            hcl2.evaluate(depends_on, context)
            for depends_on in self.payload.get(DEPENDS_ON_KEY, [])
        )

    def should_timeout(self, task, context):
        if "_timeout" not in self.payload:
            return None
        _timeout = hcl2.evaluate(self.payload["_timeout"], context)
        assert isinstance(_timeout, (int, float))
        return _timeout

    def should_rerun(self, task, context):  # pylint: disable=too-many-branches
        if "_retry" not in self.payload:
            return task.run

        _retry = hcl2.evaluate(self.payload.get("_retry", {}), context)
        _retry_params = {}
        stop_after = _retry.get("stop_after", "1 times")
        stopers = []
        for _stop_after in stop_after.split("|"):
            _stop_after = _stop_after.strip()
            if "times" in _stop_after:
                attempts = int(_stop_after.replace("times", "").strip())
                stoper = stop_after_attempt(attempts)
            elif "seconds" in _stop_after:
                seconds = float(_stop_after.replace("seconds", "").strip())
                stoper = stop_after_delay(seconds)
            else:
                raise ValueError(f"invalid _retry.stop_after: {_stop_after}")
            stopers.append(stoper)

        _retry_params["stop"] = reduce(lambda a, b: a | b, stopers)
        _retry_params["wait"] = _retry.get("wait", None)
        _retry_params["reraise"] = True
        _retry_params["after"] = after_log(logger, logging.DEBUG)
        return retry(**_retry_params)(task.run)

    def eval_payload(self, context):
        return hcl2.evaluate(
            {k: v for k, v in self.payload.items() if not k.startswith("_")},
            context,
        )

    async def run(self, context):
        """Run a task."""
        if self.type == "hcl2_template":
            context = dict(
                context,
                **hcl2.evaluate(self.payload.get("context", {}), context),
            )

        if not self.should_run(context):
            logger.info('"%s" is canceled due to falsy deps.', str(self))
            return TaskResult(TaskStatus.CANCELED)

        _payload = self.eval_payload(context)
        context["task"][self.type][self.name].update(_payload)

        task_result = TaskResult(TaskStatus.PENDING)

        try:
            logger.info('"%s" is started.', str(self))
            if isinstance(self.runner, Flow):
                task = self.runner.as_task(_payload)
            else:
                task = self.runner(**_payload)

            if isinstance(task, FlowRunTask):
                task.namespace = str(self)

            task_run = self.should_rerun(task, context)
            task_result.result = (
                await asyncio.wait_for(
                    task_run()
                    if inspect.iscoroutinefunction(task.run)
                    else utils.to_thread(task_run),
                    timeout=self.should_timeout(task, context),
                )
                or {}
            )
            task_result.result.update(_payload)
            logger.info('"%s" is successful.', str(self))
        except Exception as err:  # pylint: disable=broad-except
            task_result.exception = err
            logger.info('"%s" is failed.', str(self))
            traceback.print_exc()

        return task_result


class FlowRunTask:
    def __init__(
        self,
        path=None,
        source=None,
        module=None,
        flow=None,
        vars=None,
        export=None,
    ):
        self.path = path
        self.source = source
        self.module = module
        self.flow = flow
        self.vars = vars or {}
        self.export = export or []
        self.namespace = ""

    async def run(self):
        flow = Flow.load(
            path=self.path,
            source=self.source,
            module=self.module,
            flow=self.flow,
        )
        for task in flow:
            task.set_namespace(self.namespace)

        flow_context = await flow.run(vars=self.vars)

        if flow.exception:
            raise flow.exception

        return {
            key: hcl2.evaluate(hcl2.loads(value, "eval"), flow_context)
            for export in self.export
            for key, value in export.items()
        }


class SequentialRunner:
    """This runner runs the flow tasks sequentially."""

    def __init__(self, flow):
        self.flow = flow
        self.results = {}

    def check_depends_on(self, task):
        for upstream_task in self.flow.graph.predecessors(task):
            if self.results[upstream_task].status in (
                TaskStatus.FAILED,
                TaskStatus.CANCELED,
            ):
                return False
        return True

    async def run_task(self, task, context):
        if not self.check_depends_on(task):
            logger.info(
                '"%s" is canceled due to previous task failed run.',
                f"task.{task.type}.{task.name}",
            )
            return TaskResult(TaskStatus.CANCELED)

        task_result = await task.run(context)

        if task_result.status == TaskStatus.SUCCESS:
            context["task"][task.type][task.name] = task_result.result

        return task_result

    async def run(self, context):
        """Run flow tasks."""
        for task in self.flow:
            self.results[task] = await self.run_task(task, context)


# pylint: disable=too-many-public-methods
class Flow:
    """Flow object manages the flow graph and the order of task executions."""

    def __init__(self, name, runner_cls=None):
        self.name = name
        self.graph = networkx.DiGraph()
        self.runner = (runner_cls or SequentialRunner)(self)
        self.vars = {}
        self.functions = {}

    def __iter__(self):
        """Iterate through all tasks in a dependent order."""
        try:
            yield from networkx.topological_sort(self.graph)
        except networkx.exception.NetworkXUnfeasible as err:
            raise RunflowAcyclicTasksError(str(err)) from err

    @property
    def exception(self):
        return next(
            (
                task_result.exception
                for task_result in self.runner.results.values()
                if task_result.status == TaskStatus.FAILED
            ),
            None,
        )

    @classmethod
    def from_spec(cls, source):
        """Load flow from a .hcl file content."""
        try:
            flow = hcl2.loads(source)
        except LarkError as err:
            raise RunflowSyntaxError(str(err)) from err

        assert "flow" in flow, "Need a flow block"
        assert len(flow["flow"]) == 1, "Runflow spec should have only one flow"

        flow_spec = flow["flow"][0]
        flow_name, flow_body = next(iter(flow_spec.items()))
        flow = cls(name=flow_name)
        flow.load_flow_spec_body(flow_body)
        return flow

    @classmethod
    def from_specfile(cls, path):
        """Load flow from a given file path."""
        with open(path) as file:
            flow_spec = file.read()
        return cls.from_spec(flow_spec)

    @classmethod
    def load(cls, path=None, source=None, module=None, flow=None):
        if path:
            return Flow.from_specfile(path)

        if source:
            return Flow.from_spec(source)

        if module:
            return import_module(module)

        return flow

    def add_task(self, task):
        """Add task to flow graph."""
        self.graph.add_node(task)

    def set_dependency(self, task, depends_on):
        """Let `task` depends on `depends_on`,

        e.g. `depends_on` is a predecessor edge of `task`.

        """
        self.graph.add_edge(depends_on, task)

    def set_default_var(self, name, value):
        """Set default value for variable."""
        self.vars[name] = value

    def load_function(self, func_name, import_string):
        """Load the imported function to task func namespace."""
        function = utils.import_module(import_string)
        self.functions[func_name] = function

    # pylint: disable=no-self-use
    def load_flow_tasks_from_spec(self, tasks_spec):
        """Load the `task` blocks."""
        for task_spec in tasks_spec:
            for task_type in task_spec:
                task_class = get_task_class(task_type)
                for task_name in task_spec[task_type]:
                    task_payload = dict(task_spec[task_type][task_name])
                    yield Task(task_type, task_class, task_name, task_payload)

    def load_task_by_task_reference(self, depends_on):
        """Find task by a reference like `task.TASK_TYPE.TASK_NAME`."""
        task_key = depends_on.split(".")
        assert len(task_key) == 3 and task_key[0] == "task"

        _, task_type, task_name = task_key

        for task in self.graph.nodes:
            if task.type == task_type and task.name == task_name:
                return task

        raise RunflowSyntaxError(
            f"Task depends on {task_key} "
            f"but the dependent task does not exist"
        )

    def load_flow_tasks_dependencies(self, task):
        """Find task dependencies."""
        deps_set = set()
        for key, value in task.payload.items():
            hcl2.resolve_deps(key, deps_set)
            hcl2.resolve_deps(value, deps_set)

        for dep in deps_set:
            yield self.load_task_by_task_reference(dep)

    def set_tasks_dependencies(self):
        """Walk the task graph and sort out the task dependencies."""
        for task in self.graph.nodes:
            explicit_deps = self.load_flow_tasks_dependencies(task)
            for dep in explicit_deps:
                self.set_dependency(task, dep)

    def load_flow_variables(self, vars_spec):
        """Load the `variable` block."""
        for var_spec in vars_spec:
            var_name = next(iter(var_spec.keys()))
            var_value_spec = next(iter(var_spec.values()))
            var_value = config(
                f"RUNFLOW_VAR_{var_name}", default=None
            ) or var_value_spec.get("default", None)
            self.set_default_var(var_name, var_value)

    # pylint: disable=no-self-use
    def load_flow_imported_tasks(self, tasks):
        """Load the `import.tasks` attribute."""
        for task_name, task_impl in tasks.items():
            register_task_class(task_name, task_impl)

    def load_flow_imported_functions(self, functions):
        """Load the `import.functions` attribute."""
        for func_name, func_import in functions.items():
            self.load_function(func_name, func_import)

    def load_flow_imports(self, imports):
        """Load the `import` block."""
        for _import in imports:
            self.load_flow_imported_tasks(_import.get("tasks", []))
            self.load_flow_imported_functions(_import.get("functions", {}))

    def load_flow_tasks(self, tasks):
        for task in self.load_flow_tasks_from_spec(tasks):
            self.add_task(task)

    def load_flow_spec_body(self, spec):
        """Load the body of a flow block."""
        self.load_flow_imports(spec.get("import", []))
        self.load_flow_variables(spec.get("variable", []))
        self.load_flow_tasks(spec.get("task", []))
        self.set_tasks_dependencies()

    def make_run_context(self, vars=None):
        """Prepare the context for a task run."""
        context = {
            "var": dict(self.vars, **dict(vars or {})),
            "task": {},
            "func": self.functions,
        }
        for task in self:
            context["task"].setdefault(task.type, {})
            context["task"][task.type].setdefault(task.name, {})
        return context

    def as_task(self, vars=None):
        return FlowRunTask(flow=self, vars=vars)

    async def run(self, vars=None):
        """Run a flow."""
        context = self.make_run_context(vars)
        await self.runner.run(context)
        return context
