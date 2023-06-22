from typing import Union, List
from . import Cipher
from cryptography.fernet import Fernet, MultiFernet


class FernetCipher(Cipher):
    def __init__(self, key: Union[bytes, List[bytes]]):
        if not isinstance(key, list):
            key = [key]
        self._fernet = MultiFernet(fernets=[Fernet(key=k) for k in key])

    def encrypt(self, value: bytes) -> bytes:
        return self._fernet.encrypt(value)

    def decrypt(self, value: bytes) -> bytes:
        return self._fernet.decrypt(value)
