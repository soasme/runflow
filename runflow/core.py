import argparse
import re
import sys
import logging
import asyncio

import lark
import hcl2
import jinja2
import networkx

from .errors import RunflowReferenceError

logger = logging.getLogger(__name__)


class Command:

    def __init__(self, command):
        self.command = command

    async def run(self, context):
        logger.info(f"Runflow command is started: {self.command}")
        proc = await asyncio.create_subprocess_shell(
            self.command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        stdout, stderr = await proc.communicate()
        stdout = stdout.decode('utf-8').strip()
        stderr = stderr.decode('utf-8').strip()

        if proc.returncode == 0:
            logger.info(f"Runflow command is successful: {self.command}")
        else:
            logger.error(f"Runflow command is failed: {self.command}\n{stderr}")

        # TBD: return a response, indicating task run status and result.
        return dict(
            returncode=proc.returncode,
            stdout=stdout,
            stderr=stderr,
        )

class Task:

    def __init__(self, type, name, payload):
        self.type = type
        self.name = name
        self.payload = payload

    def __repr__(self):
        return f'Task(type={self.type}, name={self.name}, payload={self.payload})'

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, o):
        return self.type == o.type and self.name == o.name

    async def run(self, context):
        if self.type == 'command':
            command_tpl = jinja2.Template(
                self.payload['command'],
                variable_start_string="${",
                variable_end_string="}",
                undefined=jinja2.StrictUndefined,
            )
            try:
                command = Command(command_tpl.render(context))
            except jinja2.exceptions.UndefinedError as e:
                raise RunflowReferenceError(str(e).replace("'dict object'", f"{self}"))
            return await command.run(context)
        raise ValueError(f"Invalid task type `{self.type}`")

class SequentialRunner:

    def __init__(self, flow):
        self.flow = flow

    async def run(self, context):
        for task in self.flow:
            result = await task.run(context)
            for result_key, result_value in result.items():
                context['task'][task.type][task.name][result_key] = result_value

class Flow:

    def __init__(self, name, runner_cls=None):
        self.name = name
        self.G = networkx.DiGraph()
        self.runner = (runner_cls or SequentialRunner)(self)

    def __iter__(self):
        return reversed(list(networkx.topological_sort(self.G)))

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

    def make_run_context(self, variables=None):
        context = { 'var': variables or {}, 'task': {}}
        for task in self:
            context['task'].setdefault(task.type, {})
            context['task'][task.type][task.name] = task.payload
        return context

    async def run(self, variables=None):
        context = self.make_run_context(variables)
        return await self.runner.run(context)


def run(path, vars=None):
    flow = Flow.from_specfile(path)
    coro = flow.run(vars or {})

    asyncio.run(coro)
