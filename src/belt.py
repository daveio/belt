import click

from audioinfo_commands import get_audioinfo
from crypt_commands import crypt_rand, crypt_simple, crypt_wireguard
from dns_commands import dns_flush, dns_lookup, dns_sec
from domain_commands import domain_expiry, domain_ns
from meta import version as belt_version
from tls_commands import tls_cert, tls_ciphers


@click.group()
@click.version_option(version=belt_version)
def cli() -> None:
    pass


@cli.group()
def crypt() -> None:
    pass


@cli.group()
def domain() -> None:
    pass


@cli.group()
def dns() -> None:
    pass


@cli.group()
def tls() -> None:
    pass


@cli.command()
def version() -> None:
    click.echo(f"belt, version {belt_version}")


@cli.command()
@click.argument("path", nargs=1, type=click.Path(), default=".")
def audioinfo(path: click.Path) -> None:
    click.echo(get_audioinfo(path))


@crypt.command()
def rand() -> None:  # DevSkim: ignore DS148264
    click.echo(crypt_rand())


@crypt.command()
def simple() -> None:
    click.echo(crypt_simple())


@crypt.command()
@click.option(
    "-s",
    "--script",
    is_flag=True,
    show_default=True,
    default=False,
    help="Print keys for a script, as PRIVATEKEY PUBLICKEY",
)
def wireguard(script: bool) -> None:
    click.echo(crypt_wireguard(script))


@dns.command()
def flush() -> None:
    click.echo(dns_flush())


@dns.command()
@click.argument("query", nargs=1, type=str, required=True)
@click.argument("record_type", nargs=1, type=str, required=False, default="A")
@click.option("-s", "--server", type=str, help="DNS server to use", default="1.1.1.1")
@click.option(
    "-r", "--root", is_flag=True, help="Use root servers directly", default=False
)
def lookup(query: str, record_type: str, server: str, root: bool) -> None:
    click.echo(dns_lookup(query, record_type, server, root))


@dns.command()
def sec() -> None:
    click.echo(dns_sec())


@domain.command()
def expiry() -> None:
    click.echo(domain_expiry())


@domain.command()
def ns() -> None:
    click.echo(domain_ns())


@tls.command()
def cert() -> None:
    click.echo(tls_cert())


@tls.command()
def ciphers() -> None:
    click.echo(tls_ciphers())


if __name__ == "__main__":
    cli()
