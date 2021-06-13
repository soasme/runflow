import re

import hcl2
import lark
from decouple import config

from .errors import RunflowSyntaxError, RunflowTaskTypeError


def load_flow_tasks_from_spec(flow, tasks_spec):
    from .core import Task

    for task_spec in tasks_spec:
        task_type, _task_spec = next(iter(task_spec.items()))
        task_name, _task_spec = next(iter(_task_spec.items()))
        task_payload = {k: (v[0] if len(v) == 1 else v) for k, v in _task_spec.items()}

        if task_type not in flow.exts:
            raise RunflowTaskTypeError(f'unknown task type {task_type}')

        task_class = flow.exts[task_type]

        yield Task(task_type, task_class, task_name, task_payload)

def load_task_by_task_reference(flow, depends_on):
    m = re.match(r"\${([^}]+)}", depends_on)
    if not m:
        raise RunflowSyntaxError(
            f"Task parameter \"depends_on\" should "
            f"refer to a valid task: {depends_on}"
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

    return task_dependency

def load_flow_explicit_tasks_dependencies(flow, task):
    for depends_on in task.payload.get('depends_on', []):
        yield load_task_by_task_reference(flow, depends_on)

def _load_flow_implicit_tasks_dependencies(deps_set, value):
    if isinstance(value, str):
        task_keys = re.findall(r"\${([^}]+)}", value)
        if not task_keys:
            return
        for task_key in task_keys:
            if not task_key.startswith('task.'):
                continue
            deps_set.add(task_key)

    elif isinstance(value, list):
        for _value in value:
            _load_flow_implicit_tasks_dependencies(deps_set, _value)

    elif isinstance(value, dict):
        for _value in value.values():
            _load_flow_implicit_tasks_dependencies(deps_set, _value)

def load_flow_implicit_tasks_dependencies(flow, task):
    deps_set = set()
    for key, value in task.payload.items():
        if key == 'depends_on':
            continue
        _load_flow_implicit_tasks_dependencies(deps_set, value)
    for task_key in deps_set:
        task_key = task_key.split('.')
        task_dependency = next((t for t in flow.G.nodes if t.name == task_key[2] and t.type == task_key[1]), None)
        if not task_dependency:
            raise RunflowSyntaxError(
                f'Task depends_on {task_key} '
                f'but the dependent task does not exist'
            )

        yield task_dependency

def load_flow_tasks_dependencies(flow):
    for task in flow.G.nodes:
        for task_dependency in load_flow_explicit_tasks_dependencies(flow, task):
            flow.set_dependency(task, task_dependency)

        for task_dependency in load_flow_implicit_tasks_dependencies(flow, task):
            flow.set_dependency(task, task_dependency)

def load_flow_default_vars(flow, vars_spec):
    for var_spec in vars_spec:
        var_name = next(iter(var_spec.keys()))
        var_value_spec = next(iter(var_spec.values()))
        var_default_value = var_value_spec.get('default', [])
        try:
            var_value = (
                config(f'RUNFLOW_VAR_{var_name}', default=None)
                or var_default_value[0]
            )
        except IndexError:
            raise RunflowReferenceError(f"var.{var_name} is not provided.")
        flow.set_default_var(var_name, var_value)

def load_flow_extensions(flow, extensions):
    if not extensions:
        return

    for ext in extensions[0]:
        flow.load_extension(ext)

def loads(spec):
    from .core import Flow

    try:
        flow = hcl2.loads(spec)
    except lark.exceptions.LarkError as e:
        raise RunflowSyntaxError(str(e))

    assert 'flow' in flow, 'Need a flow block'
    assert len(flow['flow']) == 1, 'One Runflow spec should have only one flow'

    flow = flow['flow'][0]
    flow_name, flow_spec = next(iter(flow.items()))

    flow = Flow(name=flow_name)

    load_flow_extensions(flow, flow_spec.get('extensions', []))
    load_flow_default_vars(flow, flow_spec.get('variable', []))

    for task in load_flow_tasks_from_spec(flow, flow_spec.get('task', [])):
        flow.add_task(task)

    load_flow_tasks_dependencies(flow)

    return flow
