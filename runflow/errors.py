"""Runflow errors."""


class RunflowError(Exception):
    """Base Runflow error."""


class RunflowSyntaxError(RunflowError):
    """The flow spec has a syntax error."""


class RunflowReferenceError(RunflowError):
    """The variable is not declared in the flow spec."""


class RunflowTaskTypeError(RunflowError):
    """The task type is not registered."""


class RunflowTaskError(RunflowError):
    """The task execution is failed."""


class RunflowAcyclicTasksError(RunflowError):
    """The task has circular dependency."""
