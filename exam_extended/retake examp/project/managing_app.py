import os

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users = []
        self.vehicles = []
        self.routes = []
        self.users_dict = {}
        self.vehicles_dict = {}
        self.valid_type_vehicles = {
            'PassengerCar': PassengerCar,
            'CargoVan': CargoVan
        }

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self.__user_by_driving_license_number(driving_license_number)
        if user:
            return f"{driving_license_number} has already been registered to our platform."
        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        self.users_dict[driving_license_number] = user
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):

        self.__validate_vehicle_type(vehicle_type)
        vehicle = self.__vehicle_by_license_plate_number(license_plate_number)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."
        class_name = self.valid_type_vehicles[vehicle_type]
        vehicle = class_name(brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        self.vehicles_dict[license_plate_number] = vehicle
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        locked = 0
        self.__validate_route_non_exist(start_point, end_point, length, locked)
        route_id = len(self.routes) + 1
        route = Route(start_point, end_point, length, route_id)
        if locked == 1:
            route.is_locked = True
        route.is_locked = False
        self.__lock_same_route(route)
        self.routes.append(route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = self.__user_by_driving_license_number(driving_license_number)
        vehicle = self.__vehicle_by_license_plate_number(license_plate_number)
        route = self.__route_by_id(route_id)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if route.is_locked:
            return "Route {route_id} is locked! This trip is not allowed."
        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()
        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        selected_vehicle = []
        for vehicle in self.vehicles:
            if vehicle.is_damaged:
                selected_vehicle.append(vehicle)
        selected_vehicle.sort(key=lambda x: (x.brand, x.model))
        while count > 0:
            if len(selected_vehicle) < count:
                break
            i = 0
            selected_vehicle[i].is_damaged = False
            selected_vehicle[i].battery_level = 100
            i += 1
            count -= 1

        return f"{count} vehicles were successfully repaired!"

    def users_report(self):
        self.users.sort(key=lambda x: x.rating, reverse=True)
        result = '*** E-Drive-Rent ***' + '\n' + os.linesep.join(m.__str__() for m in self.users)
        return result

    def __user_by_driving_license_number(self, driving_license_number) -> User:
        return self.users_dict.get(driving_license_number, None)

    def __vehicle_by_license_plate_number(self, license) -> BaseVehicle:
        return self.vehicles_dict.get(license, None)

    def __validate_vehicle_type(self, vehicle_type):
        for model in self.valid_type_vehicles.keys():
            if model != vehicle_type:
                return f"Vehicle type {vehicle_type} is inaccessible."

    def __validate_route_non_exist(self, start_point, end_point, length, locked):
        result = ''
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                result =f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                result =  f"{start_point}/{end_point} shorter route had already been added to our platform."
            if route.start_point == start_point and route.end_point == end_point and route.length >= length:
                result = locked + 1
        return result


    def __route_by_id(self, route_id):
        for route in self.routes:
            if route.route_id == route_id:
                return route

    def __lock_same_route(self, route):
        for r in self.routes:
            if route.start_point == r.start_point and route.end_point == r.end_point:
                r.is_locked = True
