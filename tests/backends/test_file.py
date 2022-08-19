import json
import tempfile
from uuid import uuid4

import pytest

from dcache.backends import File
from dcache.exceptions import NotExistError


def test_set():
    backend, key, value = File(), str(uuid4()), str(uuid4())

    backend[key] = value

    with open(backend.filepath) as f:
        data = json.load(f)

    assert data == {key: value}


def test_get_not_existing_file():
    backend = File(filepath="/not_exist")

    with pytest.raises(NotExistError):
        backend[str(uuid4())]


def test_get_empty_file():
    backend = File()

    with pytest.raises(NotExistError):
        backend[str(uuid4())]


def test_get_not_existing_value():
    backend, key, other_key = File(), str(uuid4()), str(uuid4())

    backend[key] = ""

    with pytest.raises(NotExistError):
        backend[other_key]


def test_set_and_get():
    backend, key, value = File(), str(uuid4()), str(uuid4())

    backend[key] = value

    assert backend[key] == value


def test_custom_filepath():
    with tempfile.NamedTemporaryFile() as f:
        backend = File(filepath=f.name)
        key, value = str(uuid4()), str(uuid4())

        backend[key] = value

        data = json.load(f)

        assert data == {key: value}
