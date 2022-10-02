import click

from .check import check


@click.group()
def cli():
    """
    It is a Command Line
    for efficient process management
    of gps-of-gps.

    \b
    Commands:
        check
        create [Options]
        find [Options]
    """
    pass

cli.add_command(check)
