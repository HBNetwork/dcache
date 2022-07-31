def dhash(func, *args, **kwargs):
    """
    Create a unique hash from the union of func, args and kwargs.
    """
    key = args
    key += (func,)
    for item in kwargs.items():
        key += item
    return hash(key)
