from unittest import TestCase
from car_manager import Car


class TestCar(TestCase):
    MAKE = 'Honda'
    MODEL = 'Jazz'
    FUEL_CONSUMPTON = 6.5
    FUEL_CAPACITY = 50
    FUEL_AMOUNT = 0

    def setUp(self) -> None:
        car = Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTON, self.FUEL_CAPACITY)

    def test_init(self):
        self.assertEqual()


    def test_make__when_is_null_or_empty__espected_raise(self):
        pass


    def test_make__when_is_not_null_or_empty__espected_value(self):
        pass

    def test_model__when_is_null_or_empty__espected_raise(self):
        pass

    def test_model__when_is_not_null_or_empty__espected_value(self):
        pass

    def test_fuel_cpacity__when_value_zero_or_negative__espected_raise(self):
        pass

    def test_fuel_cpacity__when_value_is_positive(self):
        pass

    def test_fuel_amount__when_value_is_negative__espected_raise(self):
        pass

    def test_fuel_amount__when_value_is_positive(self):
        pass

    def test_refuel__when_value_zero_or_negative__espected_raise(self):
        pass

    def test_refuel__when_value_is_positive(self):
        pass

    def test_refuel__when_value_is_equal_to_fuel_capacity(self):
        pass

    def test_distance__when_fuel_not_enough__espected_raise(self):
        pass

    def test_distance__espected_fuel_decrace(self):
        pass
