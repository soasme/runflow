import sys
import subprocess

import hcl2

class InvalidFlow(Exception):
    pass

def runflow(definition):
    flow_wrapper = hcl2.loads(definition)

    if 'flow' not in flow_wrapper:
        raise InvalidFlow('No `flow` block defined.')

    if len(flow_wrapper['flow']) > 1:
        raise InvalidFlow('Multiple `flow` blocks defined.')

    flow = flow_wrapper['flow'][0]

    flow_name = list(flow.keys())[0]
    flow_spec = flow[flow_name]

    flow_tasks = []
    for task in flow_spec.get('task', []):
        for task_type, named_task in task.items():
            for task_name, task_definition in named_task.items():
                if task_type == 'command':
                    command = task_definition['command'][0]
                    proc = subprocess.run(command, capture_output=True)
                    sys.stdout.write(proc.stdout.decode('utf-8'))
                else:
                    raise NotImplementedError(f'Invalid task type: {task_type}.')
