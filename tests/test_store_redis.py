from unittest import mock
from sigilo.stores.redis import RedisStore


def test_redis_store_set_and_get():
    store = RedisStore(redis_url="redis://")

    with mock.patch.object(store, "_redis", FakeRedis()):
        store.set("key1", b"value1")
        assert store.get("key1") == b"value1"


class FakeRedis:
    def __init__(self):
        self._data = {}

    def get(self, key):
        return self._data[key]

    def set(self, key, value):
        self._data[key] = value
