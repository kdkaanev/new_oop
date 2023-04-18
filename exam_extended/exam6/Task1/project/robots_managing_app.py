from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_TYPE_OF_SERVICES = {'MainService':MainService,
                              'SecondaryService':SecondaryService}
    VALID_TYPE_OF_ROBOTS = ['MaleRobot', 'FemaleRobot']

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        '''

         The method creates a service of the given type and adds it to the [services] collection.
                  All service names will be unique.
              - If the service type is not valid:
                  -> raise an Exception with the following message:"Invalid service type!"
              - else:
                  -> create the service
                  -> add it to the [services]
                  -> return the following message: "{service_type} is successfully added."

                  Valid types of services are: "MainService" and "SecondaryService"

          '''

        self.__validate_valid_type_servise(service_type)
        service_name = self.__get_servise_by_type(service_type)
        service = service_name(service_type)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        '''
        The method creates a robot of the given type and adds it to the [robots] collection.
                    All robots' names will be unique.
            - If the robot type is not valid:
                -> raise an Exception with the following message: "Invalid robot type!"
            -else:
                -> create the robot, add it to the [robots]
                -> return the following message: "{robot_type} is successfully added."

                    •	Valid types of robots are: "MaleRobot" and "FemaleRobot"

        '''
        self.__validate_valid_type_robot(robot_type)
        robot_class = getattr(BaseService, robot_type)
        robot = robot_class(name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."


    def add_robot_to_service(self, robot_name: str, service_name: str):
        pass

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        pass

    def feed_all_robots_from_service(self, service_name: str):
        pass

    def service_price(self, service_name: str):
        pass

    def __str__(self):
        pass

    def __validate_valid_type_servise(self, service_type):
        if service_type not in self.VALID_TYPE_OF_SERVICES:
            raise Exception("Invalid service type!")

    def __validate_valid_type_robot(self, robot_type):
        if robot_type not in self.VALID_TYPE_OF_ROBOTS:
            raise Exception("Invalid robot type!")

    def __get_servise_by_type(self, service_type):
        for key, value in self.VALID_TYPE_OF_SERVICES.items():
            if service_type == key:
                return value
