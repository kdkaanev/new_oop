class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        need_fuel = self.DEFAULT_FUEL_CONSUMPTION * kilometers
        if self.fuel >= need_fuel:
            self.fuel -= need_fuel

