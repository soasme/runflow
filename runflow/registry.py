from .errors import RunflowReadOnlyError
from .utils import import_module


task_implementations = {
    "flow_run": {
        "class": "runflow.contribs.flow:FlowRunTask",
    },
    "bash_run": {
        "class": "runflow.contribs.bash:BashRunTask",
    },
    "docker_run": {
        "class": "runflow.contribs.docker:DockerRunTask",
    },
    "file_read": {
        "class": "runflow.contribs.local_file:FileReadTask",
    },
    "file_write": {
        "class": "runflow.contribs.local_file:FileWriteTask",
    },
    "hcl2_template": {
        "class": "runflow.contribs.template:Hcl2TemplateTask",
    },
    "http_request": {
        "class": "runflow.contribs.http:HttpRequestTask",
    },
    "sql_exec": {
        "class": "runflow.contribs.sql:SqlExecTask",
    },
    "sql_row": {
        "class": "runflow.contribs.sql:SqlRowTask",
    },
}


class ImmutableDict(dict):
    """Dict but immutable.

    Getitem is allowed; set/del/clear are disallowed.
    """

    def __init__(self, target):
        super().__init__()
        self.target = target

    def __getitem__(self, item):
        return self.target[item]

    def __delitem__(self, key):
        raise RunflowReadOnlyError

    def __setitem__(self, key, value):
        raise RunflowReadOnlyError

    def clear(self):
        raise RunflowReadOnlyError

    def __contains__(self, item):
        return item in self.target

    def __iter__(self):
        yield from self.target


_registry = {}

registry = ImmutableDict(_registry)


def register_task_class(name, cls, overwrite=False):
    """Register a task class with a name."""
    if isinstance(cls, str):
        if name in task_implementations and not overwrite:
            raise ValueError(
                f"Task name {name} has been taken in the "
                "default task implementation."
            )
        task_implementations[name] = {"class": cls}
        return
    if name in registry and not overwrite:
        raise ValueError(f"Task name {name} has been taken in the registry.")
    if not hasattr(cls, "run"):
        raise ValueError("cls is not runnable.")
    _registry[name] = cls


def get_task_class(name):
    """Get the task class by name."""
    if name not in registry:
        if name not in task_implementations:
            raise ValueError(f"Unknown task type: {name}")
        impl = import_module(task_implementations[name]["class"])
        register_task_class(name, impl)
    return registry[name]
