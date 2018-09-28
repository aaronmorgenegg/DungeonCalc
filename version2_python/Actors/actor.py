from abc import ABC, abstractmethod

class Actor(ABC):
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def printSimple(self):
        pass

    @abstractmethod
    def printDetail(self):
        pass
