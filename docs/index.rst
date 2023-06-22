Sigilo 🤫
=========

Sigilo provides a secure way to store and retrieve sensitive information like
passwords, OAuth access tokens, credit card numbers, etc.

For example, to store a secret on `redis <https://redis.io/>`_ using
:class:`sigilo.Sigilo`::

   from sigilo import Sigilo
   from sigilo.stores.redis import RedisStore
   from sigilo.ciphers.fernet import FernetCipher

   # Put this somewhere safe!
   key = "Ds205mteCt42PaW35TQWtj5LgUB3A541EVf9wy8OyOI="
   cipher = FernetCipher(key)
   store = RedisStore("redis://localhost:6379/0")

   sigilo = Sigilo(store=store, cipher=cipher)
   sigilo.set("key1", b"secret value")


To retrieve the secret::

   sigilo.get("key1")
   # returns b"secret value"


Installation
------------

Sigilo requires Python 3.8 or newer to run.

.. code-block:: bash

   pip install sigilo[redis,cryptography]



API Reference
-------------

.. toctree::
   :maxdepth: 3

   api


Additional Notes
----------------

.. toctree::
   :maxdepth: 2

   contributing


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
