======
dcache
======


.. image:: https://img.shields.io/pypi/v/dcache.svg
        :target: https://pypi.python.org/pypi/dcache
        :alt: PyPI

.. image:: https://coveralls.io/repos/github/HBN3tw0rk/dcache/badge.svg?branch=master
        :target: https://coveralls.io/github/HBN3tw0rk/dcache?branch=master
        :alt: Coverage Status

.. image:: https://readthedocs.org/projects/dcache/badge/?version=latest
        :target: https://dcache.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

Distributed Cache for Humans


* Documentation: https://dcache.readthedocs.io.


Installation
------------

.. code:: bash

    pip install dcache




How to Use
----------
- TODO


Contributing
------------
Contributions are welcome, feel free to open an Issue or Pull Request.

Pull requests must be for the `develop` branch.

.. code:: bash

    git clone https://github.com/HBN3tw0rk/dcache
    cd dcache
    git checkout develop
    python -m venv .venv
    pip install -r requirements_dev.txt
    pre-commit install
    pytest


Pitch (Portuguese)
------------------
* Part 1: https://www.loom.com/share/ee553d6915ca4dc5ba8609d48b59bd55
* Part 2: https://www.loom.com/share/50cb4ff9560943879d78864f5fa1b4e0


What is
-------
* distributed cache for humans
* simple API like `lru_cache`
* multiple backends
* easy to switch the backend
* good documentation


API
---

dcache
^^^^^^

.. code:: python

    from dcache import dcache

    @dcache
    def slow_function(n):
        return n ** 1000


dcache vs redis
^^^^^^^^^^^^^^^

.. code:: python

    import redis
    redis = redis.Redis(host='localhost', port=6379, db=0)

    def slow_function(n):
        cached = redis.get(n)
        if cached:
            return cached
        value = n ** 1000
        redis.set(n, value)
        return value

    def slow_function2(n):
        cached = redis.get(n)
        if cached:
            return cached
        value = n ** 1000
        redis.set(n, value)
        return value

.. code:: python

    from dcache import cache
    from dcache.backends import RedisBackend

    cache = dcache(RedisBackend(host='localhost', port=6379, db=0))

    @cache
    def slow_function(n):
        return n ** 1000

    @cache
    def slow_function2(n):
        return n ** 1000


real example
^^^^^^^^^^^^

.. code:: python

    def process(id, input):
        cache_path = get_content_cache_path(id, input)

        if resource.file_exist(cache_path):
            return resource.get_json(cache_path)

        response = slow_function(id, input)
          resource.put_json(body=response, file_path=cache_path)
        return response

.. code:: python

    from dcache import dcache
    from dcache.backends import S3Backend

    @dcache(S3Backend())
    def process(id, input):
        return slow_function(id, input)


Ideas
-----

* integration tests using containers

multiple backends
^^^^^^^^^^^^^^^^^

.. code:: python

    from dcache import dcache
    from dcache.backends import InMemoryBackend, RedisBackend

    @dcache(multiple=[
        InMemoryBackend(),
        RedisBackend(host='localhost', port=6379, db=0),
    ])
    def slow_function(n):
            return n ** 1000

1. search on the in-memory cache;
2. if exists, return, if not, search on Redis;
3. * if exists on Redis, save in memory and return;
4. * if not, exists on Redis, run the `slow_function`, save on Redis, save in-memory and return;

* doesn't run if already returned


MVP
---
* in memory


Roadmap
-------
* backends: Redis, Memcached, Filesystem, database, S3, etc.
* multiple backends
* plugins
