import sys
import logging
import argparse

def cli_abort(message):
    print(message, file=sys.stderr)
    exit(1)

def cli_parser():
    parser = argparse.ArgumentParser(
        prog='runflow',
        description='Runflow - a lightweight workflow engine.',
    )
    parser.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'CRITICAL'],
        default='INFO',
        help='Logging level',
    )

    subparsers = parser.add_subparsers(help='', dest='subparser_name')

    run_parser = subparsers.add_parser('run', help='Run a Runflow spec file')
    run_parser.add_argument('specfile', help='Path to a Runflow spec file')
    run_parser.add_argument('--var', dest='vars', action='append',
                        help='Provide variables for a Runflow job run')
    return parser

def cli_parser_var(var):
    key, value = var.split('=')
    return key.strip(), value.strip()

def cli_subcommand_run(args):
    vars = []
    for var in args.vars or []:
        try:
            vars.append(cli_parser_var(var))
        except ValueError:
            cli_abort(f"Invalid --var option: {var}")

    from .core import run
    run(args.specfile, dict(vars))

def cli(argv=None):
    parser = cli_parser()
    args, rest = parser.parse_known_args(argv)

    logging_format = '[%(asctime)-15s] %(message)s'
    logging.basicConfig(level=args.log_level, format=logging_format)

    if args.subparser_name == 'run':
        cli_subcommand_run(args)
    else:
        parser.print_help()
