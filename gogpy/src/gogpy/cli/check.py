import click

from gogpy.usecase.check_count import execute


@click.command()
def check():
    """
    This is the Command Line
    to check the number of data.

    \b
    Usage:
        $ gogpy check

    """

    execute()
