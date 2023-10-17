mod whois;

fn main() {
    whois::whois_toy_impl().expect("WHOIS toy implementation failed to run");
}
