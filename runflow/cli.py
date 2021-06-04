from .core import run

def parse_cli_var(var):
    key, value = var.split('=')
    return key.strip(), value.strip()

def cli():
    parser = argparse.ArgumentParser(description='Runflow - a lightweight workflow engine.')
    parser.add_argument('specfile', help='Path to a Runflow spec file')
    parser.add_argument('--var', dest='vars', action='append',
                        help='Provide variables for a Runflow job run')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'CRITICAL'],
                        default='INFO', help='Logging level')
    args = parser.parse_args()

    logging_format = '[%(asctime)-15s] %(message)s'
    logging.basicConfig(level=args.log_level, format=logging_format)

    vars = []
    for var in args.vars or []:
        try:
            vars.append(parse_cli_var(var))
        except ValueError:
            print(f"Invalid --var option: {var}", file=sys.stderr)
            exit(1)

    run(args.specfile, dict(vars))
