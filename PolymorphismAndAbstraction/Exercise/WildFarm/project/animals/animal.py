from abc import ABC, abstractmethod


class Animal(ABC):
    DEFAULT_FOOD_EATEN = 0

    def __init__(self, name: str, weight: float, food_eaten=None):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten if food_eaten else self.DEFAULT_FOOD_EATEN

    @abstractmethod
    def make_sound(self):
        pass


class Bird(Animal, ABC):
    def __init__(self, wing_size: float, name: str, weight: float):
        super().__init__(name, weight)
        self.wing_size = wing_size


class Mammal(Animal, ABC):
    def __init__(self, living_region: str, name: str, weight: float):
        super().__init__(name, weight)
        self.living_region = living_region
