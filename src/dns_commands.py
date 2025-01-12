from platform import system

# trunk-ignore(bandit/B404)
from subprocess import CalledProcessError, run

from click import echo
from dns.resolver import resolve_at


def dns_lookup(query: str, record_type: str, server: str, root: bool) -> str:
    answer = resolve_at(server, query, record_type)
    return answer.rrset


def dns_sec() -> str:
    return "dns_sec: Not yet implemented"


def dns_flush() -> str:
    commands = {
        "windows": "ipconfig /flushdns",
        "darwin": "sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder",
        "linux": "sudo systemd-resolve --flush-caches",
    }
    os_name = system().lower()
    try:
        if os_name in commands.keys():
            if os_name == "darwin":
                real_os_name = "Darwin (macOS)"
            else:
                real_os_name = os_name.capitalize()
            echo(f"{real_os_name} detected, executing: {commands[os_name]}", err=True)
            result = run(
                commands[os_name],
                shell=True,  # trunk-ignore(bandit/B602): hardcoded commands
                capture_output=True,
                text=True,
            )
            echo(f"DNS cache flushed successfully.\n{result.stdout}", err=True)
        else:
            echo(f"Unsupported operating system: {os_name}", err=True)
    except CalledProcessError as e:
        echo(f"Error flushing DNS cache: {e.stderr}", err=True)
