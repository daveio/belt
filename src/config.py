from pathlib import Path
from textwrap import dedent

from cryptography.fernet import Fernet
from xdg import BaseDirectory
from yaml import safe_load


def get_config() -> dict:
    config_path = Path(BaseDirectory.save_config_path("belt") + "/config.yaml")

    if config_path.is_file():
        with open(config_path, "r") as file:
            yaml = safe_load(file)
    else:
        with open(config_path, "w") as file:
            file.write(
                dedent(
                    f"""
                    # Example configuration file for Belt
                    #
                    # crypt:
                    #   env:    # Environment variable to use for generating random passwords
                    #   key:    # Key to use for encryption/decryption
                    # dns:
                    #   server: # DNS server to use for DNS lookups
                    #   root:   # Whether to use root servers directly for DNS lookups
                    #
                    crypt:
                        env: BELT_CRYPT_KEY
                        key: {Fernet.generate_key().decode()}
                    dns:
                        server: 1.1.1.1
                        root: false
                    """
                )
            )
        with open(config_path, "r") as file:
            yaml = safe_load(file)

    config = {}

    if yaml.get("crypt"):
        config["crypt"] = {}
        if yaml["crypt"].get("env"):
            config["crypt"]["env"] = yaml["crypt"]["env"]
        else:
            config["crypt"]["env"] = None
        if yaml["crypt"].get("key"):
            config["crypt"]["key"] = yaml["crypt"]["key"]
        else:
            config["crypt"]["key"] = None
    else:
        config["crypt"] = {"env": None, "key": None}

    if yaml.get("dns"):
        config["dns"] = {}
        if yaml["dns"].get("server"):
            config["dns"]["server"] = yaml["dns"]["server"]
        else:
            config["dns"]["server"] = None
        if yaml["dns"].get("root"):
            config["dns"]["root"] = yaml["dns"]["root"]
        else:
            config["dns"]["root"] = False
    else:
        config["dns"] = {"server": None, "root": False}

    return config


def crypt_key() -> str:
    # check configured env var, otherwise use key from config
    return "not yet implemented"
