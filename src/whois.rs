use chrono::format::ParseError;
use chrono::{DateTime, Utc};
use date_component::date_component;
use whois_rust::{WhoIs, WhoIsLookupOptions};
use whoisthere::parse_info;

mod data;

pub(crate) fn whois_toy_impl() -> Result<(), ParseError> {
    // TODO: async
    let domain_name = "dave.io";

    let whois =
        WhoIs::from_string(&data::WHOIS_SERVERS_JSON).expect("Failed to contact WHOIS server");

    let whois_response = whois
        .lookup(WhoIsLookupOptions::from_string(domain_name).expect("Failed to parse domain name"))
        .expect("Failed to look up domain");

    let parsed_response = parse_info(domain_name, &whois_response);

    let expiry = DateTime::parse_from_rfc3339(&parsed_response.expiration_date)
        .expect("Failed to parse expiration date")
        .with_timezone(&Utc);

    let now = Utc::now();

    let date_diff = date_component::calculate(&now, &expiry);

    println!("{:?}", date_diff);

    Ok(())
}
