from sigilo.ciphers.fernet import FernetCipher

KEY = b"TapEC8fPmSVx0t0fXBRNxykVpRXP-P9FKP5xzmrVn24="


def test_fernet_encrypt():
    cipher = FernetCipher(key=KEY)
    assert b"secret" not in cipher.encrypt(b"secret")


def test_fernet_decrypt():
    cipher = FernetCipher(key=KEY)
    assert (
        cipher.decrypt(
            b"gAAAAABkk2IH668wy0dl3Zxdw4tKwDcQLK22MsEjQvrtRpT0vGvfjNJxPN8h12SHK3J3KS6oxq6ct2vquYAEu0JzdsTZ8UNPQg=="
        )
        == b"secret"
    )
