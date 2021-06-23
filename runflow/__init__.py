"""
runflow - a tool to define an run your workflows.
"""
__all__ = [
    "Flow",
    "Task",
    "runflow",
    "cli",
    "RunflowError",
    "RunflowSyntaxError",
    "RunflowReferenceError",
    "RunflowTaskTypeError",
    "RunflowTaskError",
    "RunflowAcyclicTasksError",
    "load_flow",
    "runflow",
]

from . import autoloader  # noqa
from .cli import cli
from .core import Flow, Task
from .errors import (
    RunflowAcyclicTasksError,
    RunflowError,
    RunflowReferenceError,
    RunflowSyntaxError,
    RunflowTaskError,
    RunflowTaskTypeError,
)
from .run import load_flow, runflow

if __name__ == "__main__":
    cli()
