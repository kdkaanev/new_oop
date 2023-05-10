from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    DEFAULT_FOOD_EATEN = 0

    def __init__(self, name: str, weight: float, food_eaten=None):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten if food_eaten else self.DEFAULT_FOOD_EATEN

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food: Food):
        pass


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {round(self.weight,2)}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {round(self.weight,2)}, {self.living_region}, {self.food_eaten}]"
