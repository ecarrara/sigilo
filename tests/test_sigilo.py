from sigilo import Sigilo
from sigilo.ciphers.fernet import FernetCipher
from sigilo.stores.memory import MemoryStore
from sigilo.ciphers.plain import PlainCipher


def test_sigilo_get_and_set_plain_cipher():
    sigilo = Sigilo(store=MemoryStore(), cipher=PlainCipher())
    sigilo.set("key1", b"secret value")
    assert sigilo.get("key1") == b"secret value"


def test_sigilo_get_and_set_fernet_cipher():
    key = b"ctx3IAegELgETEJD4ScwjH7vLB8V9cuQ7teiRd80EJk="
    sigilo = Sigilo(store=MemoryStore(), cipher=FernetCipher(key=key))
    sigilo.set("key1", b"secret value")
    assert sigilo.get("key1") == b"secret value"
