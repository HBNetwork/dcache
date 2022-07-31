from dcache.backends import InMemory
from dcache.exceptions import NotExistError
from dcache.keys import dhash


class Dcache:
    def __init__(self, backend=None, key=dhash):
        self._backend = backend or InMemory()
        self._key = key

    def __call__(self, func):
        return _Cached(func, self._backend, self._key)


class _Cached:
    def __init__(self, func, backend, key):
        self.func = func
        self.backend = backend
        self.key = key

    def __call__(self, *args, **kwargs):
        key = self.key(self.func, *args, **kwargs)

        try:
            return self.backend[key]
        except NotExistError:
            value = self.func(*args, **kwargs)
            self.backend[key] = value
            return value
