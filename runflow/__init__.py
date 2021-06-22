__all__ = [
    'Flow', 'Task', 'runflow',
    'cli',
    'RunflowError', 'RunflowSyntaxError',
    'RunflowReferenceError', 'RunflowTaskTypeError',
    'RunflowTaskError', 'RunflowAcyclicTasksError',
]

from .core import Flow, Task, run as runflow
from .cli import cli
from .errors import (
    RunflowError, RunflowSyntaxError, RunflowReferenceError,
    RunflowTaskTypeError, RunflowTaskError, RunflowAcyclicTasksError,
)

if __name__ == '__main__':
    cli()
