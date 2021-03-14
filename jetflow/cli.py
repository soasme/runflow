import logging

import click

logger = logging.getLogger(__name__)

@click.group()
@click.option('--log-level', '-l', default='INFO')
def entry(log_level):
    """jetflow - a framework for building real-time data pipelines."""
    logging.basicConfig(level=log_level)

@entry.command()
@click.argument('module')
def build(module):
    logger.info(f'build task - {module}')

@entry.command()
def worker():
    logger.info(f'worker started.')
