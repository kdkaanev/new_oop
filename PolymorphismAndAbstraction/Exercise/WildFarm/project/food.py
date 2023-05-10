from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity: int):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self):
        pass


class Fruit(Food):
    def __init__(self):
        pass


class Meat(Food):
    def __init__(self):
        pass


class Seed(Food):
    def __init__(self):
        pass
