import logging

import click

logger = logging.getLogger(__name__)

@click.group()
@click.option('--log-level', '-l', default='INFO')
def entry(log_level):
    """runflow - a tool to define and run workflows."""
    logging.basicConfig(level=log_level)

@entry.command()
@click.argument('module')
def build(module):
    logger.info(f'building task - {module}')
    from .utils import import_string
    module = import_string(module)

    if not callable(module):
        click.echo('build task failed - not runnable', err=True)
        click.abort(1)

    instance = module()

    if hasattr(instance, 'run'):
        instance.run()
        return

    if hasattr(instance, '__call__'):
        instance()
        return



@entry.command()
def worker():
    logger.info(f'worker started.')
