from abc import abstractmethod

from abc import ABC


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
        trip = self.fuel_quantity - (self.fuel_consumption + 0.9) * distance
        if trip > 0:
            self.fuel_quantity = trip
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption) -> None:
        super().__init__()
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        trip = self.fuel_quantity - (self.fuel_consumption + 1.6) * distance
        if trip > 0:
            self.fuel_quantity = trip
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)