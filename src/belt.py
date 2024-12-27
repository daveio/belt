import click

from keypair import compose_keypair
from audioinfo import compose_audioinfo
from dns import dns_lookup
from meta import version as belt_version


@click.group()
@click.version_option(version=belt_version)
def cli() -> None:
    pass


@cli.command()
def version() -> None:
    click.echo(f"belt, version {belt_version}")


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

@cli.group()
def dns() -> None:
    pass

@dns.command()
@click.argument("query", nargs=1, type=str, required=True)
@click.argument("record_type", nargs=1, type=str, required=False, default="A")
@click.option("-s", "server", type=str, help="DNS server to use", default="1.1.1.1")
@click.option("-r", "root", type=bool, help="Use root servers directly", default=False)
def lookup(query: str, record_type: str, server: str, root: bool) -> None:
    click.echo(dns_lookup(query, record_type, server, root))


if __name__ == "__main__":
    cli()
