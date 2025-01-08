from os import getenv
from pathlib import Path
from textwrap import dedent

from xdg import BaseDirectory
from yaml import safe_load

from cryptor import Cryptor


def get_config() -> dict:
    config_path = Path(BaseDirectory.save_config_path("belt") + "/config.yaml")

    if config_path.is_file():
        pass
    else:
        with open(config_path, "w") as file:
            file.write(
                dedent(
                    f"""
                    # Example configuration file for Belt
                    #
                    # crypt:
                    #   env:    # Environment variable containing the key to use for encryption/decryption
                    #           # This supercedes any key specified in the 'key' field
                    #   key:    # Key to use for encryption/decryption
                    #   warned: # Whether the user has been warned about the consequences of losing the key
                    # dns:
                    #   server: # DNS server to use for DNS lookups
                    #   root:   # Whether to use root servers directly for DNS lookups
                    #
                    crypt:
                        env: BELT_CRYPT_KEY
                        key: {Cryptor.keygen(raw=False)}
                        warned: false
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
        if yaml["crypt"].get("warned"):
            config["crypt"]["warned"] = yaml["crypt"]["warned"]
        else:
            config["crypt"]["warned"] = False
    else:
        config["crypt"] = {"env": None, "key": None, "warned": False}

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


def get_key() -> str:
    config = get_config()
    env = config.get("crypt").get("env")
    if env:
        key = getenv(env)
    if key is None:
        key = config.get("crypt").get("key")
    if key:
        return key
    return None
