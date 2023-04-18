from abc import ABC, abstractmethod


class BaseRobot(ABC):
    MIN_PRICE = 0.0
    EMPTY_STRING_ERR_MESSAGE = 'cannot be empty!'
    VALUE_ERR_MESSAGE = f'cannot be less than or equal to {MIN_PRICE}!'

    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_non_empty_string(value)
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__validate_non_empty_string(value)
        self.__kind = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__validate_value_above_zerro(value)
        self.__price = value

    @abstractmethod
    def eating(self):
        pass

    def __validate_non_empty_string(self, value):
        if value == '' and all(char.isspace() for char in value):
            raise ValueError(f'Robot {value}{self.EMPTY_STRING_ERR_MESSAGE}')

    def __validate_value_above_zerro(self, value):
        if value <= self.MIN_PRICE:
            raise ValueError(f'Robot price {self.VALUE_ERR_MESSAGE}')
