from dcache.exceptions import NotExistError


class Base:
    def __getitem__(self, key):
        raise NotImplementedError

    def __setitem__(self, key, value):
        raise NotImplementedError


class InMemory(dict, Base):
    def __getitem__(self, *args, **kwargs):
        try:
            return super().__getitem__(*args, **kwargs)
        except KeyError as e:
            raise NotExistError from e
