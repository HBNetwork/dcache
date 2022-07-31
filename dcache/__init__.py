from dcache.backends import InMemory
from dcache.exceptions import NotExistError


def make_hash(func, *args, **kwargs):
    key = args
    key += (func,)
    for item in kwargs.items():
        key += item
    return hash(key)


class Cached:
    def __init__(self, func, backend, make_key):
        self.func = func
        self.backend = backend
        self.make_key = make_key

    def __call__(self, *args, **kwargs):
        key = self.make_key(self.func, *args, **kwargs)

        try:
            return self.backend[key]
        except NotExistError:
            value = self.func(*args, **kwargs)
            self.backend[key] = value
            return value


class Dcache:
    def __init__(self, backend=None, make_key=make_hash):
        self._backend = backend or InMemory()
        self._make_key = make_key

    def __call__(self, func):
        return Cached(func, self._backend, self._make_key)


cache = Dcache()
