import json

from dcache.serializers import Json


def test_dumps():
    serializer, data = Json(), {"key": "value"}
    assert serializer.dumps(data) == json.dumps(data)


def test_loads():
    serializer, serialized_data = Json(), json.dumps({"key": "value"})
    assert serializer.loads(serialized_data) == json.loads(serialized_data)
