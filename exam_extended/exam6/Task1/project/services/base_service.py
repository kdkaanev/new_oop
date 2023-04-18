from abc import ABC, abstractmethod


class BaseService(ABC):
    MIN_CAPACITY = 0
    VALUE_ERR_MESSAGE = f'cannot be less than or equal to {MIN_CAPACITY}!'
    EMPTY_STRING_ERR_MESSAGE = 'cannot be empty!'

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_non_empty_string(value)
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__validate_value_above_zerro(value)
        self.__capacity = value

    @abstractmethod
    def details(self):
        pass

    def __validate_non_empty_string(self, value):
        if value == '' and all(char.isspace() for char in value):
            raise ValueError(f'Service {value}{self.EMPTY_STRING_ERR_MESSAGE}')

    def __validate_value_above_zerro(self, value):
        if value <= self.MIN_CAPACITY:
            raise ValueError(f'Service capacity {self.VALUE_ERR_MESSAGE}')
