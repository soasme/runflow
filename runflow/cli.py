"""Command-line interface for runflow."""

import logging
import sys
from argparse import ArgumentParser, Namespace
from typing import Dict, Any

from networkx.drawing.nx_agraph import to_agraph

from . import hcl2
from .core import Flow
from .run import runflow


def cli_abort(message: str):
    """Print abort message."""
    print(message, file=sys.stderr)
    sys.exit(1)


def cli_parser():
    """Parse runflow arguments."""
    parser = ArgumentParser(
        prog="runflow",
        description="Runflow - a lightweight workflow engine.",
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "CRITICAL"],
        default="INFO",
        help="Logging level",
    )

    subparsers = parser.add_subparsers(help="", dest="subparser_name")

    run_parser = subparsers.add_parser("run", help="Run a Runflow spec file")
    run_parser.add_argument("specfile", help="Path to a Runflow spec file")
    run_parser.add_argument(
        "--var",
        dest="vars",
        action="append",
        help="A variable key-value pair",
    )
    run_parser.add_argument(
        "--var-file",
        dest="varfiles",
        action="append",
        help="Path to a file including variables",
    )

    visualize_parser = subparsers.add_parser(
        "visualize", help="Visualize a Runflow spec file"
    )
    visualize_parser.add_argument(
        "specfile", help="Path to a Runflow spec file"
    )
    visualize_parser.add_argument(
        "--output",
        default="visualize.svg",
        help="The output of the flow graph visualization file.",
    )

    return parser


def cli_parser_var(var: str):
    """Parse runflow `--var` value."""
    key, value = var.split("=")
    return key.strip(), value.strip()


def _load_specfile(specfile: str):
    if specfile.endswith(".hcl"):
        return {"path": specfile}

    if specfile == "-":
        return {"source": sys.stdin.read()}

    return {"module": specfile}


def cli_subcommand_run(args: Namespace):
    """Command: `runflow run`."""
    vars = {}
    for varfile in args.varfiles or []:
        with open(varfile) as file:
            ctx: Dict[str, Any] = {}
            for key, value in hcl2.loads(file.read()).items():
                vars[hcl2.evaluate(key, ctx)] = hcl2.evaluate(value, ctx)

    for var in args.vars or []:
        try:
            key, value = cli_parser_var(var)
            vars[key] = value
        except ValueError:
            cli_abort(f"Invalid --var option: {var}")

    loader = _load_specfile(args.specfile)
    runflow(vars=vars, **loader)


def cli_subcommand_visualize(args: Namespace):
    """Command: `runflow visualize`."""
    flow = Flow.load(**_load_specfile(args.specfile))
    agraph = to_agraph(flow.graph)
    agraph.layout("dot")
    agraph.draw(args.output)


SUBCOMMANDS = dict(
    run=cli_subcommand_run,
    visualize=cli_subcommand_visualize,
)


def cli(argv=None):
    """Command: `runflow`."""
    parser = cli_parser()
    args, _rest = parser.parse_known_args(argv)

    logging_format = "[%(asctime)-15s] %(message)s"
    logging.basicConfig(level=args.log_level, format=logging_format)

    if args.subparser_name in SUBCOMMANDS:
        SUBCOMMANDS[args.subparser_name](args)
    else:
        parser.print_help()
