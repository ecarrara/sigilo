from . import Store
from pymemcache.client.base import Client


class MemcacheStore(Store):
    def __init__(self, memcache_host: str, memcache_port: int):
        self._client = Client((memcache_host, memcache_port))

    def get(self, key: str) -> bytes:
        value = self._client.get(key)
        if value is None:
            raise KeyError(f'"{key}" not found.')
        return value

    def set(self, key: str, value: bytes):
        self._client.set(key, value)
