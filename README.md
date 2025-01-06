# `belt`: a cli toolbox

## Installation

### `pipx` (recommended)

I would suggest installation using `pipx`. This keeps `belt` from affecting anything else in your default `pip` environment.

First install `pipx`-

```shell
pip install pipx
```

Then use `pipx` to install `belt-cli`-

```shell
pipx install belt-cli
```

By default, this will put the executable in `~/.local/bin`- make sure it's in your shell`$PATH`or`fish_user_paths`.

### `pip`

If you don't want to use `pipx` then you can simply do

```shell
pip install belt-cli
```

## Configuration

### Path

```text
~/.config/belt/config.yaml
```

### Generating Configuration

If no config exists, a sample config (with random key) is generated when you first run `belt`.

If you want to be explicit about it you can run `belt init`, which will **overwrite any existing config and keys** so think about it first.

`belt` will warn you and request confirmation if an existing config exists.

### Sample Configuration

```yaml
crypt:
  env: BELT_CRYPT_KEY
  key: AGE-SECRET-KEY-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  warned: false
dns:
  server: 1.1.1.1
  root: false
```

## Key Management

Make sure you **back up your key**, whether you store it in the config file or the environment. A password manager is an excellent choice for this.

If you use `chezmoi`to manage your dotfiles, add the `belt` config file with encryption. Though you then need to make sure you back up your `chezmoi` key.

Without the key, anything you encrypt with `belt crypt simple encrypt`will be unrecoverable.
