import inspect
import traceback
import logging
import enum

import lark
import networkx
from decouple import config

from .errors import (
    RunflowSyntaxError, RunflowTaskTypeError, RunflowReferenceError,
    RunflowAcyclicTasksError,
)
from . import hcl2, utils


logger = logging.getLogger(__name__)


class TaskStatus(enum.Enum):
    PENDING = enum.auto()
    SUCCESS = enum.auto()
    FAILED = enum.auto()


class TaskResult:

    def __init__(self, status):
        self.status = status
        self._result = None
        self._exception = None

    @property
    def result(self):
        if self._exception:
            raise ValueError(
                'Task has no result due to a failed run.'
            ) from self._exception
        return self._result

    @result.setter
    def result(self, _result):
        self.status = TaskStatus.SUCCESS
        self._result = _result

    @property
    def exception(self):
        if self._result:
            raise ValueError('Task has no exception due to a successful run.')
        return self._exception

    @exception.setter
    def exception(self, _exception):
        self.status = TaskStatus.FAILED
        self._exception = _exception


class Task:

    def __init__(self, type, runner, name, payload):
        self.type = type
        self.runner = runner
        self.name = name
        self.payload = payload

    def __repr__(self):
        return (
            f'Task(type={self.type}, '
            f'name={self.name}, '
            f'payload={self.payload})'
        )

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, o):
        return self.type == o.type and self.name == o.name

    async def run(self, context):
        if self.type == "hcl2_template":
            context = dict(context, **hcl2.evaluate(
                self.payload.get('context', {}),
                context
            ))

        payload = hcl2.evaluate(self.payload, context)

        task_result = TaskResult(TaskStatus.PENDING)

        _payload = dict(payload)
        # this is handled by runflow, not by runner.
        _payload.pop('depends_on', None)

        task = self.runner(**_payload)

        try:
            logger.info(f'"task.{self.type}.{self.name}" is started.')
            task_result.result = (
                await task.run(context)
                if inspect.iscoroutinefunction(task.run)
                else await utils.to_thread(task.run, context)
            )
            logger.info(f'"task.{self.type}.{self.name}" is successful.')
        except Exception as e:
            task_result.exception = e
            logger.info(f'"task.{self.type}.{self.name}" is failed.')
            traceback.print_exc()
        return task_result


class SequentialRunner:

    def __init__(self, flow):
        self.flow = flow

    async def run(self, context):
        runnable = True
        for task in self.flow:
            if not runnable:
                logger.info(
                    f'"task.{task.type}.{task.name}" is canceled '
                    'due to previous task failed run.'
                )
                continue

            task_result = await task.run(context)
            if task_result.status == TaskStatus.FAILED:
                runnable = False
                continue

            context['task'][task.type][task.name] = task_result.result


class Flow:

    default_tasks = {
        'runflow.contribs.bash:BashRunTask',
        'runflow.contribs.docker:DockerRunTask',
        'runflow.contribs.local_file:FileReadTask',
        'runflow.contribs.local_file:FileWriteTask',
        'runflow.contribs.template:Hcl2TemplateTask',
        'runflow.contribs.http:HttpRequestTask',
        'runflow.contribs.sql:SqlExecTask',
        'runflow.contribs.sql:SqlRowTask',
        'runflow.contribs.flow:FlowRunTask',
    }

    def __init__(self, name, runner_cls=None):
        self.name = name
        self.G = networkx.DiGraph()
        self.runner = (runner_cls or SequentialRunner)(self)
        self.vars = {}

        self.exts = {}
        self.functions = {}
        self.load_default_tasks()

    def __iter__(self):
        try:
            return reversed(list(networkx.topological_sort(self.G)))
        except networkx.exception.NetworkXUnfeasible as e:
            raise RunflowAcyclicTasksError(str(e)) from e

    @classmethod
    def from_spec(cls, source):
        try:
            flow = hcl2.loads(source)
        except lark.exceptions.LarkError as e:
            raise RunflowSyntaxError(str(e))

        assert 'flow' in flow, 'Need a flow block'
        assert len(flow['flow']) == 1, 'Runflow spec should have only one flow'

        flow = flow['flow'][0]
        flow_name, flow_spec_body = next(iter(flow.items()))

        flow = cls(name=flow_name)
        flow.load_flow_spec_body(flow_spec_body)
        return flow

    @classmethod
    def from_specfile(cls, path):
        with open(path) as f:
            flow_spec = f.read()
        return cls.from_spec(flow_spec)

    def add_task(self, task):
        self.G.add_node(task)

    def set_dependency(self, task, depends_on):
        self.G.add_edge(task, depends_on)

    def set_default_var(self, name, value):
        self.vars[name] = value

    def load_task(self, import_string):
        task_class = utils.import_module(import_string)
        task_class_name = task_class.__name__
        assert task_class_name != 'Task' and task_class_name.endswith('Task')
        task_type_chunks = utils.split_camelcase(task_class_name)
        assert task_type_chunks[-1] == 'Task'
        task_type = '_'.join(task_type_chunks[:-1]).lower()
        self.exts[task_type] = task_class

    def load_default_tasks(self):
        for mod in self.default_tasks:
            self.load_task(mod)

    def load_function(self, import_string):
        function = utils.import_module(import_string)
        func_name = import_string.split(':')[-1].replace('.', '_')
        self.functions[func_name] = function

    def make_run_context(self, vars=None):
        context = {
            'var': dict(self.vars, **dict(vars or {})),
            'task': {},
            'func': self.functions,
        }
        for task in self:
            context['task'].setdefault(task.type, {})
            context['task'][task.type][task.name] = task.payload
        return context

    def load_flow_tasks_from_spec(self, tasks_spec):
        for task_spec in tasks_spec:
            task_type, _task_spec = next(iter(task_spec.items()))
            task_name, _task_spec = next(iter(_task_spec.items()))
            task_payload = {k: v for k, v in _task_spec.items()}

            if task_type not in self.exts:
                raise RunflowTaskTypeError(f'unknown task type {task_type}')

            task_class = self.exts[task_type]
            yield Task(task_type, task_class, task_name, task_payload)

    def load_task_by_task_reference(self, depends_on):
        if not isinstance(depends_on, hcl2.Interpolation):
            raise RunflowSyntaxError(
                f"Task parameter \"depends_on\" should "
                f"refer to a valid task: {depends_on}"
            )

        task_key = depends_on.expr.attr_chain
        if task_key[0] != 'task':
            raise RunflowSyntaxError(
                "Task parameter \"depends_on\" should refer "
                f"to a valid task: {depends_on}"
            )

        task_dependency = next(
            t for t in self.G.nodes if t.name == task_key[2]
        )
        if task_dependency.type != task_key[1]:
            raise RunflowSyntaxError(
                f'Task parameter "depends_on" {depends_on}, '
                f'but task {task_key[2]} is of type {task_key[1]}'
            )

        return task_dependency

    def load_flow_explicit_tasks_dependencies(self, task):
        for depends_on in task.payload.get('depends_on', []):
            yield self.load_task_by_task_reference(depends_on)

    def load_flow_implicit_tasks_dependencies(self, task):
        deps_set = set()
        for key, value in task.payload.items():
            if key == 'depends_on':
                continue
            hcl2.resolve_deps(value, deps_set)
        for task_key in deps_set:
            task_key = task_key.split('.')
            task_dependency = next((
                t for t in self.G.nodes
                if t.name == task_key[2] and t.type == task_key[1]
            ), None)
            if not task_dependency:
                raise RunflowSyntaxError(
                    f'Task depends_on {task_key} '
                    f'but the dependent task does not exist'
                )

            yield task_dependency

    def set_tasks_dependencies(self):
        for task in self.G.nodes:
            explicit_deps = self.load_flow_explicit_tasks_dependencies(task)
            for dep in explicit_deps:
                self.set_dependency(task, dep)

            implicit_deps = self.load_flow_implicit_tasks_dependencies(task)
            for dep in implicit_deps:
                self.set_dependency(task, dep)

    def load_flow_default_vars(self, vars_spec):
        for var_spec in vars_spec:
            var_name = next(iter(var_spec.keys()))
            var_value_spec = next(iter(var_spec.values()))
            var_default_value = var_value_spec.get('default', [])
            try:
                var_value = (
                    config(f'RUNFLOW_VAR_{var_name}', default=None)
                    or var_default_value
                )
            except IndexError:
                raise RunflowReferenceError(f"var.{var_name} is not provided.")
            self.set_default_var(var_name, var_value)

    def load_flow_imported_tasks(self, tasks):
        for task in tasks:
            self.load_task(task)

    def load_flow_imported_functions(self, functions):
        for function in functions:
            self.load_function(function)

    def load_flow_extensions(self, extensions):
        if not extensions:
            return

        for ext in extensions:
            self.load_flow_imported_tasks(ext.get('tasks', []))
            self.load_flow_imported_functions(ext.get('functions', []))

    def load_flow_spec_body(self, spec):
        self.load_flow_extensions(spec.get('import', []))
        self.load_flow_default_vars(spec.get('variable', []))

        for task in self.load_flow_tasks_from_spec(spec.get('task', [])):
            self.add_task(task)

        self.set_tasks_dependencies()

    async def run(self, vars=None):
        context = self.make_run_context(vars)
        return await self.runner.run(context)
