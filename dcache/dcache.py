from dcache.backends import InMemory
from dcache.exceptions import NotExistError
from dcache.keys import dhash


class Dcache:
    """
    :param backend: The backend used to cache, defaults to :class:`dcache.backends.InMemory`
    :type backend: :class:`dcache.backends.Base`, optional

    :param key: A function that will receive cached function, args and kwargs, and
        should return a unique key that will be used to distinguish the cached results,
        defaults to :func:`dcache.keys.dhash`
    :type key: function, optional
    """

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
