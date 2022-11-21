from abc import ABC, abstractmethod


class Supply(ABC):
    @abstractmethod
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"

        