"""Command-line interface for runflow."""

import argparse
import logging
import sys

from networkx.drawing.nx_agraph import to_agraph

from .run import loadflow, runflow


def cli_abort(message):
    """Print abort message."""
    print(message, file=sys.stderr)
    sys.exit(1)


def cli_parser():
    """Parse runflow arguments."""
    parser = argparse.ArgumentParser(
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
        help="Provide variables for a Runflow job run",
    )

    visualize_parser = subparsers.add_parser(
        "visualize", help="Visualize a Runflow spec file"
    )
    visualize_parser.add_argument(
        "specfile", help="Path to a Runflow spec file"
    )
    visualize_parser.add_argument(
        "--output",
        default='visualize.svg',
        help="The output of the flow graph visualization file."
    )

    return parser


def cli_parser_var(var):
    """Parse runflow `--var` value."""
    key, value = var.split("=")
    return key.strip(), value.strip()


def _load_specfile(specfile):
    if specfile.endswith(".hcl"):
        return {"path": specfile}

    if specfile == "-":
        return {"source": sys.stdin.read()}

    return {"module": specfile}


def cli_subcommand_run(args):
    """Command: `runflow run`."""
    vars = []
    for var in args.vars or []:
        try:
            vars.append(cli_parser_var(var))
        except ValueError:
            cli_abort(f"Invalid --var option: {var}")

    loader = _load_specfile(args.specfile)
    runflow(vars=dict(vars), **loader)


def cli_subcommand_visualize(args):
    """Command: `runflow visualize`."""
    flow = loadflow(**_load_specfile(args.specfile))
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
