from abc import ABC, abstractmethod


class Delicacy(ABC):
    MIN_PRICE = 0.0

    def __init__(self, name: str, portion: int, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__is_falls_name(value)
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__validate_price(value)
        self.__price = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        self.__portion = value

    @staticmethod
    def __is_falls_name(name):
        if not isinstance(name, str) or name.isspace():
            return ValueError("Name cannot be null or whitespace!")

    def __validate_price(self, price):
        if price <= self.MIN_PRICE:
            raise ValueError("Price cannot be less or equal to zero!")

    @abstractmethod
    def details(self):
        pass

    @abstractmethod
    def type(self):
        pass
