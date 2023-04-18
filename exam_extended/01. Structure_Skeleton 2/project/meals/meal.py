from abc import ABC, abstractmethod


class Meal(ABC):
    MIN_PRICE = 0.0
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.check_correct_name(value)
        self.__name =value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.check_price(value)
        self.__price = value


    @abstractmethod
    def details(self):
        pass

    @staticmethod
    def check_correct_name(value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError('Name cannot be an empty string!')

    def check_price(self, value):
        if value <= self.MIN_PRICE:
            raise ValueError('Invalid price!')


