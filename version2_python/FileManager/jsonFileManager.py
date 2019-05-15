import json

from version2_python.FileManager.dummyFileManager import DummyFileManager


class JsonFileManager(DummyFileManager):
    def save(self, data, filename):
        print(data)
        with open("{}.json".format(filename), "w") as file:
            json.dump(data, file)

    def load(self, filename):
        with open("{}.json".format(filename), "w") as file:
            data = json.load(file)
            return data
