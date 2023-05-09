from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage = None):
        self.max_mileage = max_mileage if max_mileage else self.MAX_MILEAGE
        super().__init__(brand, model, license_plate_number, max_mileage)

    def drive(self, mileage: float):
        percent = round((mileage / self.MAX_MILEAGE) * 100)
        self.battery_level -= percent
