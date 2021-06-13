class RunflowError(Exception):
    pass

class RunflowSyntaxError(RunflowError):
    pass

class RunflowReferenceError(RunflowError):
    pass

class RunflowTaskTypeError(RunflowError):
    pass

class RunflowTaskError(RunflowError):
    pass

class RunflowAcyclicTasksError(RunflowError):
    pass
