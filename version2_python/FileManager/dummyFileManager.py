class DummyFileManager:
    def save(self, data, filename):
        print("Saving {} to {}".format(data, filename))

    def load(self, filename):
        print("Loading data from {}".format(filename))
