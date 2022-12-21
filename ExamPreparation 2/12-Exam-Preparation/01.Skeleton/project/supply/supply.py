from abc import ABC, abstractmethod
from project.utill import validate

class Supply(ABC):
    MIN_ENERGY = 0
    EMPTY_STRING_ERROR_MESSAGE = "Name cannot be an empty string."
    NEGATIVE_ENERGY_ERROR_MESSAGE = "Energy cannot be less than zero."

    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_empty_string(value)
        self.__name = value



    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        self.__validate_min_number(value, self.NEGATIVE_ENERGY_ERROR_MESSAGE, self.MIN_ENERGY)
        self.__energy = value

    @property
    @abstractmethod
    def type(self):
        pass

    def details(self):
        return f"{self.type}: {self.name}, {self.energy}"

    def __validate_empty_string(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise self.EMPTY_STRING_ERROR_MESSAGE

    @staticmethod
    def __validate_min_number(value, err_message, num):
        if not isinstance(value, int) or value < num:
            raise ValueError(err_message)



