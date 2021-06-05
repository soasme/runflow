import re

import hcl2
import lark

from .errors import RunflowSyntaxError


def load_flow_tasks_from_spec(tasks_spec):
    from .core import Task

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
    for task in load_flow_tasks_from_spec(flow_spec.get('task', [])):
        flow.add_task(task)

    load_flow_tasks_dependencies(flow)
    # TBD: load variables
    return flow
