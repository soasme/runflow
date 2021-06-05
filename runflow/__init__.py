from .core import Flow, Task, run as runflow
from .errors import RunflowError, RunflowSyntaxError, RunflowReferenceError
from .cli import cli

if __name__ == '__main__':
    cli()
