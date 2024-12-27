import dns.resolver


def dns_lookup(query: str, record_type: str, server: str, root: bool) -> str:
    answer = dns.resolver.resolve_at(server, query, record_type)
    return answer.rrset
