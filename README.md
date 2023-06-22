# Sigilo 🤫

[![Documentation](https://readthedocs.org/projects/sigilo/badge/)](https://sigilo.readthedocs.io/en/latest/)
[![PyPI](https://img.shields.io/pypi/v/sigilo)](https://pypi.org/project/sigilo/)
![GitHub](https://img.shields.io/github/license/ecarrara/sigilo)

Sigilo provides a secure way to store and retrieve sensitive information like
passwords, OAuth access tokens, credit card numbers, etc.

For example, to store a secret on [redis](https://redis.io/) using
sigilo.Sigilo:

```python
from sigilo import Sigilo
from sigilo.stores.redis import RedisStore
from sigilo.ciphers.fernet import FernetCipher

# Put this somewhere safe!
key = "Ds205mteCt42PaW35TQWtj5LgUB3A541EVf9wy8OyOI="
cipher = FernetCipher(key)
store = RedisStore("redis://localhost:6379/0")

sigilo = Sigilo(store=store, cipher=cipher)
sigilo.set("key1", b"secret value")
```

To retrieve the secret:

```python
sigilo.get("key1")
# returns b"secret value"
```

## Installation

Sigilo requires Python 3.8 or newer to run.

```bash
pip install sigilo[redis,cryptography]
```

