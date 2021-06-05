class RunflowError(Exception):
    pass

class RunflowSyntaxError(RunflowError):
    pass

class RunflowReferenceError(RunflowError):
    pass

class RunflowTaskError(RunflowError):
    pass
