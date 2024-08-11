from abc import abstractmethod, ABC


class BaseXtra(ABC):
    def new(self):
        pass

    @abstractmethod
    def Duplicate(self):
        pass
