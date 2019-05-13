import pickle

from version2_python.FileManager.dummyFileManager import DummyFileManager


class PickleFileManager(DummyFileManager):
    def save(self, data, filename):
        with open(".pk1".format(filename), "wb") as file:
            pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        with open(".pk1".format(filename), "wb") as file:
            data = pickle.load(file)
            return data
