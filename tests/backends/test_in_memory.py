import pytest

from dcache.backends import InMemory
from dcache.exceptions import NotExistError


def test_set():
    backend = InMemory()
    backend["key"] = "cached_value"


def test_get_not_exist():
    backend = InMemory()

    with pytest.raises(NotExistError):
        backend["key"]


def test_set_and_get():
    backend = InMemory()

    backend["key"] = "cached_value"

    assert backend["key"] == "cached_value"
