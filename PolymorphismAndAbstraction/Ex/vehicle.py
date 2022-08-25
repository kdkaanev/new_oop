from abc import abstractmethod


from abc import ABC
from urllib.parse import ParseResultBytes


class Vehicle(ABC):
    pass

@abstractmethod
def drive():
    pass

@abstractmethod
def refuel():
    pass

class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption) -> None:
        super().__init__()
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        self.fuel_quantity -= self.fuel_consumption * distance
        return self.fuel_quantity

    def refuel(self, fuel):
        pass

        

class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption) -> None:
        super().__init__()
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        pass

    def refuel(self, fuel):
        pass







