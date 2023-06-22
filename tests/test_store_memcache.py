from unittest import mock
from sigilo.stores.memcache import MemcacheStore


def test_memcache_store_set_and_get():
    store = MemcacheStore(memcache_host="localhost", memcache_port=11211)

    with mock.patch.object(store, "_client", FakeMemcacheClient()):
        store.set("key1", b"value1")
        assert store.get("key1") == b"value1"


class FakeMemcacheClient:
    def __init__(self):
        self._data = {}

    def get(self, key):
        return self._data.get(key)

    def set(self, key, value):
        self._data[key] = value
