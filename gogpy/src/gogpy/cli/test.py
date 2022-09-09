import click


@click.command()
# @click.option("--test", "-t", hidden=True, multiple=True)
# Argument 설명 추가
def test():
    """
    test commands;

    \b
    Usage:
        $ gogpy test [OPTIONS]

    \b
    Arguments:
        test  "Enter the test"

    \b
    Examples:
        $ gogpy test 
    """

    print("Hello")
