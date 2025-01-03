# `belt`: a cli toolbox

## Language

Python 3.12

## Config file

Format: `YAML`

Path: `~/.config/belt/config.json`

| Group   | Key      | Type   | Description                                                                 |
| ------- | -------- | ------ | --------------------------------------------------------------------------- |
| `crypt` | `env`    | `str`  | Environment variable to use for encryption key                              |
| `crypt` | `key`    | `str`  | Default key for encryption/decryption (if `crypt -> env` is empty or unset) |
| `crypt` | `warned` | `bool` | Whether the user has been warned about the consequences of losing the key   |
| `dns`   | `server` | `str`  | Default DNS server to use for lookups                                       |
| `dns`   | `root`   | `bool` | Use root servers directly for lookups                                       |

```yaml
crypt:
  env: BELT_CRYPT_KEY
  key: ELYkrte99XWbLWJckwxLHz2XZzF1mn57JsDBKX43QlQ=
  warned: false
dns:
  server: 1.1.1.1
  root: false
```

## Args and flags

### Universal flags

| Full flag               | Abbreviation  |
| ----------------------- | ------------- |
| `--config` `FILE`       | `-c` `FILE`   |
| `--env-prefix` `PREFIX` | `-e` `PREFIX` |
| `--help`                | `-h`          |
| `--in` `FILE`           | `-i` `FILE`   |
| `--out` `FILE`          | `-o` `FILE`   |
| `--verbose`             | `-v`          |
| `--version`             | `-V`          |

### Functionality selection

| Command  | Subcommand  | Function   | Positional     | Params                                 |
| -------- | ----------- | ---------- | -------------- | -------------------------------------- |
| `audio`  | `info`      |            |                |                                        |
| `crypt`  | `random`    | `hex`      | `LENGTH`       |                                        |
| `crypt`  | `random`    | `key`      |                |                                        |
| `crypt`  | `random`    | `pw`       | `LENGTH`       | `-n`, `--numbers` Add numbers          |
|          |             |            |                | `-s`, `--symbols` Add symbols          |
|          |             |            |                | `-c`, `--chbs` Use xkcd format         |
| `crypt`  | `simple`    | `decrypt`  | `<STDIN>`      | `-e`, `--env` `VAR` Use key from env   |
| `crypt`  | `simple`    | `encrypt`  | `<STDIN>`      | `-e`, `--env` `VAR` Use key from env   |
| `crypt`  | `wireguard` |            |                |                                        |
| `dns`    | `flush`     |            |                |                                        |
| `dns`    | `lookup`    |            | `QUERY`        | `-s`, `--server` `HOSTNAME` Use server |
|          |             |            | `[RECORDTYPE]` | `-r`, `--root` Use root servers        |
| `dns`    | `sec`       |            | `DOMAIN.TLD`   |                                        |
| `tls`    | `cert`      | `req`      | `COMMONNAME`   | `-c`, `--client` Request client cert   |
| `tls`    | `cert`      | `selfsign` | `COMMONNAME`   | `-c`, `--client` Generate client cert  |
| `tls`    | `ciphers`   |            | `HOSTNAME`     |                                        |
|          |             |            | `PORT`         |                                        |
| `domain` | `expiry`    |            | `DOMAIN.TLD`   |                                        |
| `domain` | `ns`        |            | `DOMAIN.TLD`   |                                        |

## Features

### 1.0

- DNS
  - Lookup
  - DNSSEC check
    - Remediation instructions
  - OS cache flush
- TLS
  - Cipher list and order
  - Certificate generation
    - All features for client or server certificate
    - Self signed
    - Certificate request
- Cryptography
  - Simple encrypt/decrypt
    - Password from readline or env var
  - Generate WireGuard keypair
  - Random generation
    - Alphanumeric + symbols
    - Alphanumeric
    - Alphabetical
    - Numeric
    - Hex
    - 0x prefixed hex
- Domain
  - Time to expiry from WHOIS
  - Nameserver lookup from WHOIS
- Audio files
  - Get sample rate and bit depth

### Planned

- Git
  - Clone
  - Pull
  - Push
  - Branch
  - Detect remote changes
- SSH
  - Tunnels
  - Connections
  - Config management
  - Cipherspec validation
    - Remediation
- DNS
  - Propagation checks
    - Multiple public resolvers
- Cloudflare
  - Clear cache
- Workspace
  - Replicate `ws` functionality
