from abc import ABC, abstractmethod


class Booth(ABC):
    MIN_CAPACITY = 0

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders = []
        self.price_for_reservation = 0
        self.is_reserved = False

    @abstractmethod
    def reserve(self, number_of_people: int):
        pass

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__validate_zerro_capacity(value)
        self.__capacity = value

    def __validate_zerro_capacity(self, capacity):
        if capacity < self.MIN_CAPACITY:
            raise ValueError("Capacity cannot be a negative number!")
