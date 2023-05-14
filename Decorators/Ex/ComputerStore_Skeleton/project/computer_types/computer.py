from abc import ABC, abstractmethod
import math


class Computer(ABC):
    NAME_ERROR_MESSAGE = ' name cannot be empty.'
    VALLID_TYPES = ["Laptop", "Desktop Computer"]

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        self.__check_valid_name(value, 'Manufacturer')
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__check_valid_name(value, 'Model')
        self.__model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"

    def __check_valid_name(self, value, name):
        if not isinstance(value, str) or value.isspace():
            raise ValueError(self.NAME_ERROR_MESSAGE + name)

    def __check_processor_is_available(self, proc, available_proc):
        if proc not in available_proc.keys():
            raise ValueError(
                f"{proc} is not compatible with desktop computer {self.manufacturer} {self.model}!"
            )

