import pickle

from version2_python.FileManager.dummyFileManager import fileManager


class PickleFileManager(fileManager):
    def save(self, data, filename):
        with open(filename+".pk1", "wb") as file:
            pickle.dump(data, file, pickle.HIGHEST_PROTOCOL)

    def load(self, filename):
        with open(filename+".pk1", "wb") as file:
            data = pickle.load(file)
            return data
