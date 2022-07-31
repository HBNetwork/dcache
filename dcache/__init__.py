from dcache.dcache import Dcache

cache = Dcache()
"""
Default in-memory cache

>>> from dcache import cache
...
>>> @cache
... def slow_function():
...     ...
...
"""
