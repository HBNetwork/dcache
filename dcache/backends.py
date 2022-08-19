import tempfile
from json.decoder import JSONDecodeError
from pathlib import Path

from dcache import serializers
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
    Backend that uses a Python dict to cache values.
    """

    def __getitem__(self, *args, **kwargs):
        """
        Override `dict.__getitem__` to raise :class:`dcache.exceptions.NotExistError`
        instead of the default KeyError.

        :raises NotExistError:
            raises when the key was not found in the backend.

        :return: cached result
        """
        try:
            return super().__getitem__(*args, **kwargs)
        except KeyError as e:
            raise NotExistError from e


class File(Base):
    def __init__(self, filepath=None, serializer=None):
        self.memory = InMemory()
        self._filepath = filepath
        self.serializer = serializer or serializers.Json()

    @property
    def filepath(self):
        if not self._filepath:
            _, self._filepath = tempfile.mkstemp()
        return Path(self._filepath)

    def __getitem__(self, key):
        try:
            with open(self.filepath, "r") as f:
                data = self.serializer.load(f)
            return data[key]
        except (FileNotFoundError, JSONDecodeError, KeyError) as e:
            raise NotExistError from e

    def __setitem__(self, key, value):
        self.memory[key] = value

        with open(self.filepath, "w") as f:
            self.serializer.dump(self.memory, f)
