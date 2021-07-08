from typing import Dict, Union, Type

from .errors import RunflowReadOnlyError
from .utils import import_module


task_implementations = {
    # Core tasks
    "bash_run": {
        "class": "runflow.contribs.bash:BashRunTask",
    },
    "flow_run": {
        "class": "runflow.core:FlowRunTask",
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
    "smtp_send": {
        "class": "runflow.contribs.mail:SmtpSendTask",
    },
    "sql_exec": {
        "class": "runflow.contribs.sql:SqlExecTask",
    },
    "sql_row": {
        "class": "runflow.contribs.sql:SqlRowTask",
    },
    # Community tasks
    "docker_run": {
        "class": "runflow.community.docker:DockerRunTask",
    },
    "feed_parse": {
        "class": "runflow.community.rss:FeedParseTask",
    },
    "pushbullet_push": {
        "class": "runflow.community.pushbullet:PushbulletPushTask",
    },
    "slack_api_call": {
        "class": "runflow.community.slack:SlackApiCallTask",
    },
}


class ImmutableDict(dict):
    """Dict but immutable.

    Getitem is allowed; set/del/clear are disallowed.
    """

    def __init__(self, target: Dict[str, dict]):
        super().__init__()
        self.target = target

    def __getitem__(self, item: str):
        return self.target[item]

    def __delitem__(self, key: str):
        raise RunflowReadOnlyError

    def __setitem__(self, key: str, value):
        raise RunflowReadOnlyError

    def clear(self):
        raise RunflowReadOnlyError

    def __contains__(self, item):
        return item in self.target

    def __iter__(self):
        yield from self.target


_registry: Dict[str, dict] = {}

registry = ImmutableDict(_registry)


def register_task_class(
    name: str, cls: Union[str, Type], overwrite: bool = False
):
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
    _registry[name] = {"class": cls}


def get_task_class(name: str):
    """Get the task class by name."""
    if name not in registry:
        if name not in task_implementations:
            raise ValueError(f"Unknown task type: {name}")
        impl = import_module(task_implementations[name]["class"])
        register_task_class(name, impl)
    return registry[name]["class"]
