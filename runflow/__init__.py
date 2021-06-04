from .core import run as runflow, RunflowError, \
        RunflowSyntaxError, RunflowReferenceError
from .cli import cli

if __name__ == '__main__':
    cli()
