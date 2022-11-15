from math import floor
from project.software import Software

class LightSoftware(Software):
    def __init__(self,name, software_type, capacity_consumption, memory_consumption):
        super().__init__(name, software_type, capacity_consumption, memory_consumption)
        self.name = name
        self.software_type = software_type
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name = 'light'):
        self.__name = name

    @property
    def software_type(self):
        return self.__softwear_type

    @software_type.setter
    def sotware_type(self, type = 'Light'):
        self.__softwear_type = type

    @property
    def capacity_consumption(self):
        return self.__capacity_consumption

    @capacity_consumption.setter
    def capacity_consumption(self, value):
        result = floor(value * 1.5)
        self.__capacity_consumption = result

    @property
    def memory_consumption(self):
        return self.__memory_consumption

    @memory_consumption.setter
    def memory_consumption(self, value):
        result = floor(value * 1.5)
        self.__memory_consumption = result


    
        


