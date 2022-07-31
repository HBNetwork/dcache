def dhash(func, *args, **kwargs):
    key = args
    key += (func,)
    for item in kwargs.items():
        key += item
    return hash(key)
