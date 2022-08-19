import json


class Base:
    def dump(self, data, file):
        raise NotImplementedError

    def dumps(self, data):
        raise NotImplementedError

    def load(self, file):
        raise NotImplementedError

    def loads(self, data):
        raise NotImplementedError


class Raw(Base):
    def dump(self, data, file):
        return file.write(data)

    def dumps(self, data):
        return data

    def load(self, file):
        return file.read()

    def loads(self, data):
        return data


class Json(Base):
    def dump(self, data, file):
        return json.dump(data, file)

    def dumps(self, data):
        return json.dumps(data)

    def load(self, file):
        return json.load(file)

    def loads(self, data):
        return json.loads(data)
