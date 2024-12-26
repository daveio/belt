import click

from keypair import compose_keypair
from audioinfo import compose_audioinfo
from meta import version as belt_version


@click.group()
def cli() -> None:
    pass


@cli.command()
def version() -> None:
    click.echo(f"belt {belt_version}")


@cli.command()
@click.option(
    "-s",
    "print_script",
    is_flag=True,
    show_default=True,
    default=False,
    help="Print keys for a script, as PRIVATEKEY PUBLICKEY",
)
def keypair(print_script: bool) -> None:
    click.echo(compose_keypair(print_script))

@cli.command()
@click.argument('path', nargs=1, type=click.Path(), default=".")
def audioinfo(path: click.Path) -> None:
    click.echo(compose_audioinfo(path))


if __name__ == "__main__":
    cli()
