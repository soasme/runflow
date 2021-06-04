import argparse
import re
import sys
import logging
import asyncio

import lark
import hcl2
import jinja2
import networkx

logger = logging.getLogger(__name__)

class RunflowError(Exception):
    pass

class RunflowSyntaxError(RunflowError):
    pass

class RunflowReferenceError(RunflowError):
    pass

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

class Flow:

    def __init__(self, name):
        self.name = name
        self.G = networkx.DiGraph()

    def add_task(self, task):
        self.G.add_node(task)

    def set_dependency(self, task, depends_on):
        self.G.add_edge(task, depends_on)

    def __iter__(self):
        return reversed(list(networkx.topological_sort(self.G)))

    async def run(self, variables=None):
        context = { 'var': variables or {}, 'task': {}}
        for task in self:
            context['task'].setdefault(task.type, {})
            context['task'][task.type][task.name] = task.payload

        for task in self:
            # TBD: use asyncio.create_task: so they can run concurrently.
            result = await task.run(context)
            for result_key, result_value in result.items():
                context['task'][task.type][task.name][result_key] = result_value


def load_flow_tasks_from_spec(tasks_spec):
    for task_spec in tasks_spec:
        task_type, _task_spec = next(iter(task_spec.items()))
        task_name, _task_spec = next(iter(_task_spec.items()))
        task_payload = {k: (v[0] if len(v) == 1 else v) for k, v in _task_spec.items()}
        yield Task(task_type, task_name, task_payload)

def load_flow_tasks_dependencies(flow):
    for task in flow.G.nodes:
        for depends_on in task.payload.get('depends_on', []):
            m = re.match(r"\${([^}]+)}", depends_on)
            if not m:
                raise RunflowSyntaxError(
                    f"Task parameter \"depends_on\" should refer to a valid task: {depends_on}"
                )
            task_key = m.group(1).strip()
            task_key = task_key.split('.')
            if task_key[0] != 'task':
                raise RunflowSyntaxError(
                    f"Task parameter \"depends_on\" should refer to a valid task: {depends_on}"
                )
            task_dependency = next(t for t in flow.G.nodes if t.name == task_key[2])
            if task_dependency.type != task_key[1]:
                raise RunflowSyntaxError(
                    f'Task parameter "depends_on" {depends_on}, '
                    f'but task {task_key[2]} is of type {task_key[1]}'
                )
            flow.set_dependency(task, task_dependency)

def load_flow_from_spec(spec):
    try:
        flow = hcl2.loads(spec)
    except lark.exceptions.LarkError as e:
        raise RunflowSyntaxError(str(e))

    assert 'flow' in flow, 'Need a flow block'
    assert len(flow['flow']) == 1, 'One Runflow spec should have only one flow'

    flow = flow['flow'][0]
    flow_name, flow_spec = next(iter(flow.items()))

    flow = Flow(name=flow_name)
    for task in load_flow_tasks_from_spec(flow_spec.get('task', [])):
        flow.add_task(task)

    load_flow_tasks_dependencies(flow)
    # TBD: load variables
    return flow

def run(path, vars=None):
    with open(path) as f:
        flow_spec = f.read()

    flow = load_flow_from_spec(flow_spec)
    asyncio.run(flow.run(vars or {}))
