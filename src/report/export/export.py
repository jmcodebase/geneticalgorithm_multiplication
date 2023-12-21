from abc import ABC, abstractmethod

class Export(ABC):
    @abstractmethod
    def Load(self,i):
        pass
    @abstractmethod
    def Export():
        pass

