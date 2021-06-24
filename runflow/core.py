"""Core module for runflow."""

import enum
import inspect
import logging
import traceback

import networkx
from decouple import config

from . import hcl2, utils
from .errors import (
    RunflowAcyclicTasksError,
    RunflowReferenceError,
    RunflowSyntaxError,
)
from .hcl2_parser import LarkError
from .registry import get_task_class, register_task_class

logger = logging.getLogger(__name__)


class TaskStatus(enum.Enum):
    """Task execution status."""

    PENDING = enum.auto()
    SUCCESS = enum.auto()
    FAILED = enum.auto()


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

    def __repr__(self):
        return (
            f"Task(type={self.type}, "
            f"name={self.name}, "
            f"payload={self.payload})"
        )

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, o):
        return self.type == o.type and self.name == o.name

    async def run(self, context):
        """Run a task."""
        if self.type == "hcl2_template":
            context = dict(
                context,
                **hcl2.evaluate(self.payload.get("context", {}), context),
            )

        payload = hcl2.evaluate(self.payload, context)

        task_result = TaskResult(TaskStatus.PENDING)

        _payload = dict(payload)
        # this is handled by runflow, not by runner.
        _payload.pop("depends_on", None)

        task = self.runner(**_payload)

        try:
            logger.info('"task.%s.%s" is started.', self.type, self.name)
            task_result.result = (
                await task.run(context)
                if inspect.iscoroutinefunction(task.run)
                else await utils.to_thread(task.run, context)
            )
            logger.info('"task.%s.%s" is successful.', self.type, self.name)
        except Exception as err:  # pylint: disable=broad-except
            task_result.exception = err
            logger.info('"task.%s.%s" is failed.', self.type, self.name)
            traceback.print_exc()
        return task_result


class SequentialRunner:
    """This runner runs the flow tasks sequentially."""

    def __init__(self, flow):
        self.flow = flow

    async def run(self, context):
        """Run flow tasks."""
        runnable = True
        for task in self.flow:
            if not runnable:
                logger.info(
                    '"%s" is canceled due to previous task failed run.',
                    f"task.{task.type}.{task.name}",
                )
                continue

            task_result = await task.run(context)
            if task_result.status == TaskStatus.FAILED:
                runnable = False
                continue

            context["task"][task.type][task.name] = task_result.result


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
            return reversed(list(networkx.topological_sort(self.graph)))
        except networkx.exception.NetworkXUnfeasible as err:
            raise RunflowAcyclicTasksError(str(err)) from err

    @classmethod
    def from_spec(cls, source):
        """Load flow from a .hcl file content."""
        try:
            flow = hcl2.loads(source)
        except LarkError as err:
            raise RunflowSyntaxError(str(err)) from err

        assert "flow" in flow, "Need a flow block"
        assert len(flow["flow"]) == 1, "Runflow spec should have only one flow"

        flow = flow["flow"][0]
        flow_name, flow_spec_body = next(iter(flow.items()))

        flow = cls(name=flow_name)
        flow.load_flow_spec_body(flow_spec_body)
        return flow

    @classmethod
    def from_specfile(cls, path):
        """Load flow from a given file path."""
        with open(path) as file:
            flow_spec = file.read()
        return cls.from_spec(flow_spec)

    def add_task(self, task):
        """Add task to flow graph."""
        self.graph.add_node(task)

    def set_dependency(self, task, depends_on):
        """Let `task` depends on `depends_on`."""
        self.graph.add_edge(task, depends_on)

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
        if not isinstance(depends_on, hcl2.Interpolation):
            raise RunflowSyntaxError(
                f'Task parameter "depends_on" should '
                f"refer to a valid task: {depends_on}"
            )

        task_key = depends_on.expr.attr_chain
        if task_key[0] != "task":
            raise RunflowSyntaxError(
                'Task parameter "depends_on" should refer '
                f"to a valid task: {depends_on}"
            )

        task_dependency = next(
            t for t in self.graph.nodes if t.name == task_key[2]
        )
        if task_dependency.type != task_key[1]:
            raise RunflowSyntaxError(
                f'Task parameter "depends_on" {depends_on}, '
                f"but task {task_key[2]} is of type {task_key[1]}"
            )

        return task_dependency

    def load_flow_explicit_tasks_dependencies(self, task):
        """Find task explicit dependencies."""
        for depends_on in task.payload.get("depends_on", []):
            yield self.load_task_by_task_reference(depends_on)

    def load_flow_implicit_tasks_dependencies(self, task):
        """Find task implicit dependencies."""
        deps_set = set()
        for key, value in task.payload.items():
            if key == "depends_on":
                continue
            hcl2.resolve_deps(value, deps_set)
        for task_key in deps_set:
            task_key = task_key.split(".")
            task_dependency = next(
                (
                    t
                    for t in self.graph.nodes
                    if t.name == task_key[2] and t.type == task_key[1]
                ),
                None,
            )
            if not task_dependency:
                raise RunflowSyntaxError(
                    f"Task depends_on {task_key} "
                    f"but the dependent task does not exist"
                )

            yield task_dependency

    def set_tasks_dependencies(self):
        """Walk the task graph and sort out the task dependencies."""
        for task in self.graph.nodes:
            explicit_deps = self.load_flow_explicit_tasks_dependencies(task)
            for dep in explicit_deps:
                self.set_dependency(task, dep)

            implicit_deps = self.load_flow_implicit_tasks_dependencies(task)
            for dep in implicit_deps:
                self.set_dependency(task, dep)

    def load_flow_default_vars(self, vars_spec):
        """Load the `variable` block."""
        for var_spec in vars_spec:
            var_name = next(iter(var_spec.keys()))
            var_value_spec = next(iter(var_spec.values()))
            var_default_value = var_value_spec.get("default", [])
            try:
                var_value = (
                    config(f"RUNFLOW_VAR_{var_name}", default=None)
                    or var_default_value
                )
            except IndexError as err:
                raise RunflowReferenceError(
                    f"var.{var_name} is not provided."
                ) from err
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

    def load_flow_extensions(self, extensions):
        """Load the `import` block."""
        if not extensions:
            return

        for ext in extensions:
            self.load_flow_imported_tasks(ext.get("tasks", []))
            self.load_flow_imported_functions(ext.get("functions", []))

    def load_flow_spec_body(self, spec):
        """Load the body of a flow block."""
        self.load_flow_extensions(spec.get("import", []))
        self.load_flow_default_vars(spec.get("variable", []))

        for task in self.load_flow_tasks_from_spec(spec.get("task", [])):
            self.add_task(task)

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
            context["task"][task.type][task.name] = task.payload
        return context

    async def run(self, vars=None):
        """Run a flow."""
        context = self.make_run_context(vars)
        return await self.runner.run(context)
