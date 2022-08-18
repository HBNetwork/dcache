from dcache.exceptions import NotExistError


class Base:
    """
    Base backend to be inherit by custom backends.

    >>> from dcache.backends import Base as BaseBackend
    ...
    >>> class CustomBackend(BaseBackend):
    ...    def __init__(self):
    ...        self.cache = {}
    ...
    ...    def __getitem__(self, key):
    ...        return self.cache[key]
    ...
    ...    def __setitem__(self, key, value):
    ...        self.cache[key] = value
    ...
    >>> backend = CustomBackend()
    >>> backend['key'] = 'value'
    >>> backend['key']
    'value'
    """

    def __getitem__(self, key):
        """
        Return the value from the backend, if exists, if not raises an exception.

        :param key: The key that will be used to lookup for the cache.

        :raises NotExistError:
            raises when the key was not found in the backend.

        :return: cached result
        """
        raise NotImplementedError

    def __setitem__(self, key, value):
        """
        Save the value into the backend.

        :param key: The key that will be used to save the value.

        :param value: The value that will be cached.
        """
        raise NotImplementedError


class InMemory(dict, Base):
    """
    InMemory backend uses a dict to save the cached values.

    >>> from dcache.backends import InMemory as InMemoryBackend
    ...
    >>> backend = InMemoryBackend()
    >>> backend['key'] = 'value'
    >>> backend['key']
    'value'
    """

    def __getitem__(self, *args, **kwargs):
        """
        Override `dict.__get__` to raise :class:`dcache.exceptions.NotExistError`
        instead of the default KeyError.

        :raises NotExistError:
            raises when the key was not found in the backend.

        :return: cached result
        """
        try:
            return super().__getitem__(*args, **kwargs)
        except KeyError as e:
            raise NotExistError from e
