import json


class Base:
    def dumps(self, data):
        raise NotImplementedError

    def loads(self, data):
        raise NotImplementedError


class Raw(Base):
    def dumps(self, data):
        return data

    def loads(self, data):
        return data


class Json(Base):
    def dumps(self, data):
        return json.dumps(data)

    def loads(self, data):
        return json.loads(data)
