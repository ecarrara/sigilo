class Cipher:
    """Common interface for encryption and decryption algorithms in Sigilo."""

    def encrypt(self, value: bytes) -> bytes:
        ...

    def decrypt(self, value: bytes) -> bytes:
        ...
