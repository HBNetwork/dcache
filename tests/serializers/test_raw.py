from uuid import uuid4

from dcache.serializers import Raw


def test_dumps():
    serializer, value = Raw(), uuid4()
    assert serializer.dumps(value) == value


def test_loads():
    serializer, value = Raw(), uuid4()
    assert serializer.loads(value) == value


def test_dumps_loads():
    serializer, value = Raw(), uuid4()
    assert serializer.dumps(value) == serializer.loads(value)
