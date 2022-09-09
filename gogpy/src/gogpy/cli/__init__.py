import click

from .test import test


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """
    Desrciption

    \b
    Action Commands:
        test  [options]
    """
    pass

cli.add_command(test)
