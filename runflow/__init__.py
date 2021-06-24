"""
runflow - a tool to define an run your workflows.
"""
__all__ = [
    "Flow",
    "Task",
    "loadflow",
    "runflow",
    "runflow_async",
    "cli",
    "registry",
    "get_task_class",
    "register_task_class",
    "RunflowError",
    "RunflowSyntaxError",
    "RunflowReferenceError",
    "RunflowTaskTypeError",
    "RunflowTaskError",
    "RunflowAcyclicTasksError",
]


try:
    from importlib.metadata import entry_points
except ImportError:  # python < 3.8
    try:
        from importlib_metadata import entry_points
    except ImportError:
        entry_points = None

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
from .registry import (
    registry,
    register_task_class,
    get_task_class,
)
from .run import loadflow, runflow, runflow_async


if entry_points is not None:
    try:
        _entry_points = entry_points()
    except TypeError:
        pass  # importlib-metadata < 0.8
    else:
        # Python 3.10+ / importlib_metadata >= 3.9.0
        _tasks = (
            _entry_points.select(group="runflow.tasks")
            if hasattr(_entry_points, "select")
            else _entry_points.get("runflow.tasks", [])
        )
        for _task in _tasks:
            register_task_class(_task.name, _task.value)


if __name__ == "__main__":
    cli()
