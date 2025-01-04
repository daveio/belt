from base64 import b64decode, b64encode
from codecs import encode
from sys import stdin, stdout
from textwrap import dedent

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from pyrage import decrypt, encrypt, x25519

from config import get_key


class WireguardKeypair:
    def __init__(self, private: str, public: str) -> None:
        self.private: str = private
        self.public: str = public

    def __repr__(self) -> str:
        return f"Keypair(private={self.private}, public={self.public})"


def crypt_random_hex() -> str:
    return "crypt_random_hex: Not yet implemented"


def crypt_random_key() -> str:
    identity = x25519.Identity.generate()
    return str(identity)


def crypt_random_pw() -> str:
    return "crypt_random_pw: Not yet implemented"


def crypt_simple_encrypt() -> str:
    key = get_key()
    plaintext = stdin.buffer.read()
    ciphertext = encrypt(plaintext, [key.to_public()])
    stdout.write(b64encode(ciphertext).decode("utf-8"))


def crypt_simple_decrypt() -> None:
    key = get_key()
    cipherb64 = stdin.buffer.read().decode("utf-8")
    ciphertext = b64decode(cipherb64)
    plaintext = decrypt(ciphertext, [key])
    stdout.buffer.write(plaintext)


def crypt_wireguard(script: bool) -> str:
    encoding: serialization.Encoding = serialization.Encoding.Raw
    priv_format: serialization.PrivateFormat = serialization.PrivateFormat.Raw
    pub_format: serialization.PublicFormat = serialization.PublicFormat.Raw
    private_key: X25519PrivateKey = X25519PrivateKey.generate()
    private_bytes: bytes = private_key.private_bytes(
        encoding=encoding,
        format=priv_format,
        encryption_algorithm=serialization.NoEncryption(),
    )
    private_text: str = encode(private_bytes, "base64").decode("utf8").strip()
    public_bytes: bytes = private_key.public_key().public_bytes(
        encoding=encoding, format=pub_format
    )
    public_text: str = encode(public_bytes, "base64").decode("utf8").strip()
    keypair = WireguardKeypair(private_text, public_text)
    if script:
        return f"{keypair.private} {keypair.public}"
    return dedent(
        f"""
        Private key : {keypair.private}
        Public key  : {keypair.public}
        """
    )
