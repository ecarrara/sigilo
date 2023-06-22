from . import Store


class MemoryStore(Store):
    def __init__(self):
        self._data: dict[str, bytes] = {}

    def get(self, key: str) -> bytes:
        return self._data[key]

    def set(self, key: str, value: bytes):
        self._data[key] = value
