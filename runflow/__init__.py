"""
runflow - a tool to define an run your workflows.
"""
__all__ = [
    'Flow', 'Task', 'runflow',
    'cli',
    'RunflowError', 'RunflowSyntaxError',
    'RunflowReferenceError', 'RunflowTaskTypeError',
    'RunflowTaskError', 'RunflowAcyclicTasksError',
    'load_flow', 'runflow',
]

from .core import Flow, Task
from .cli import cli
from .errors import (
    RunflowError, RunflowSyntaxError, RunflowReferenceError,
    RunflowTaskTypeError, RunflowTaskError, RunflowAcyclicTasksError,
)
from .run import load_flow, runflow


if __name__ == '__main__':
    cli()
