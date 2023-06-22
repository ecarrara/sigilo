from . import Store

import redis


class RedisStore(Store):
    def __init__(self, redis_url: str):
        self._redis = redis.from_url(redis_url)

    def get(self, key: str) -> bytes:
        value = self._redis.get(key)
        if value is None:
            raise KeyError(f'"{key}" not found.')
        return value

    def set(self, key: str, value: bytes):
        self._redis.set(key, value)
