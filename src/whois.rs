use chrono::format::ParseError;
use chrono::{DateTime, Duration, FixedOffset, ParseResult, Utc};
use whois_rust::{WhoIs, WhoIsLookupOptions};
use whoisthere::{parse_info, DomainProps};

pub(crate) fn whois_toy_impl() -> Result<(), ParseError> {
    // TODO: async
    let domain_name: &str = "dave.io";
    let whois: WhoIs = WhoIs::from_path("data/whois.json").unwrap();
    let result: String = whois
        .lookup(WhoIsLookupOptions::from_string(domain_name).unwrap())
        .unwrap();
    let domain_props: DomainProps = parse_info(domain_name, &result);
    let expiry: ParseResult<DateTime<FixedOffset>> =
        DateTime::parse_from_rfc3339(&domain_props.expiration_date);
    let now: DateTime<Utc> = Utc::now();
    let foo: Duration = expiry.unwrap().signed_duration_since(now);
    println!("{:?}", foo);

    Ok(())
}
