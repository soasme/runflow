import traceback
import argparse
import re
import sys
import logging
import asyncio
import enum

import lark
import hcl2
import jinja2
import networkx

from .errors import (
    RunflowReferenceError, RunflowTaskError,
    RunflowAcyclicTasksError,
)
from . import utils

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
            raise ValueError('Task has no result due to a failed run.')
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
        return f'Task(type={self.type}, name={self.name}, payload={self.payload})'

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, o):
        return self.type == o.type and self.name == o.name

    async def run(self, context):
        if self.type == "template":
            template_context = utils.render(self.payload.get('context', {}), context)
            context = dict(context, **template_context)

        try:
            payload = utils.render(self.payload, context)
        except jinja2.exceptions.UndefinedError as e:
            raise RunflowReferenceError(str(e).replace("'dict object'", f"{self}"))

        task_result = TaskResult(TaskStatus.PENDING)

        _payload = dict(payload)
        _payload.pop('depends_on', None) # this is handled by runflow, not by runner.

        task = self.runner(**_payload)

        try:
            logger.info(f'"task.{self.type}.{self.name}" is started.')
            task_result.result = await task.run(context)
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
                logger.info(f'"task.{task.type}.{task.name}" is canceled due to previous task failed run.')
                continue

            task_result = await task.run(context)
            if task_result.status == TaskStatus.FAILED:
                runnable = False
                continue

            context['task'][task.type][task.name] = task_result.result

class Flow:

    default_extensions = {
        'command': 'runflow.contribs.command.CommandTask',
        'docker_run': 'runflow.contribs.docker.DockerRunTask',
        'file_read': 'runflow.contribs.local_file.LocalFileReadTask',
        'file_write': 'runflow.contribs.local_file.LocalFileWriteTask',
        'template': 'runflow.contribs.template.TemplateTask',
        'http_request': 'runflow.contribs.http.HttpRequestTask',
        'sqlite3_exec': 'runflow.contribs.sqlite3.Sqlite3ExecTask',
        'sqlite3_row': 'runflow.contribs.sqlite3.Sqlite3RowTask',
    }

    def __init__(self, name, runner_cls=None):
        self.name = name
        self.G = networkx.DiGraph()
        self.runner = (runner_cls or SequentialRunner)(self)
        self.vars = {}

        self.exts = {}
        self.load_default_extensions()

    def __iter__(self):
        try:
            return reversed(list(networkx.topological_sort(self.G)))
        except networkx.exception.NetworkXUnfeasible as e:
            raise RunflowAcyclicTasksError(str(e))

    @classmethod
    def from_spec(cls, string):
        from .parser import loads
        return loads(string)

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

    def load_extension(self, task_type, import_string):
        self.exts[task_type] = utils.import_module(import_string)

    def load_default_extensions(self):
        for key, mod in self.default_extensions.items():
            self.load_extension(key, mod)

    def make_run_context(self, vars=None):
        context = { 'var': dict(self.vars, **dict(vars or {})), 'task': {}}
        for task in self:
            context['task'].setdefault(task.type, {})
            context['task'][task.type][task.name] = task.payload
        return context

    async def run(self, vars=None):
        context = self.make_run_context(vars)
        return await self.runner.run(context)


def run(path, vars=None):
    flow = Flow.from_specfile(path)
    coro = flow.run(vars or {})

    asyncio.run(coro)
