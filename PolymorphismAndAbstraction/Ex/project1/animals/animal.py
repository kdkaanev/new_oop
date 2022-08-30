from abc import ABC, abstractmethod

from food import Food


class Animal(ABC):
    def __init__(self, name, weight, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def alowed_feed(self):
        pass


    @property
    @abstractmethod
    def weight_incrace(self):
        pass



    def feed(self, food: Food):
        food_type = food.__class__.__name__
        if food_type not in self.alowed_feed:
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * self.weight_incrace
        



class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self,food):
        pass
