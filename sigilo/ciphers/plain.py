from . import Cipher


class PlainCipher(Cipher):
    def encrypt(self, value: bytes) -> bytes:
        return value

    def decrypt(self, value: bytes) -> bytes:
        return value
