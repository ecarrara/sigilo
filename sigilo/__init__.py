__version__ = "0.2.0"

from .ciphers import Cipher
from .stores import Store


class Sigilo:
    """Teste"""

    def __init__(self, store: Store, cipher: Cipher):
        self.store = store
        self.cipher = cipher

    def get(self, key: str) -> bytes:
        encrypted_value = self.store.get(key)
        return self.cipher.decrypt(encrypted_value)

    def set(self, key: str, plain_value: bytes):
        encrypted_value = self.cipher.encrypt(plain_value)
        return self.store.set(key, encrypted_value)
