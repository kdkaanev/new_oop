from project.hardware import Hardware

class HeavyHardware(Hardware):
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int) -> None:
        super().__init__(name, hardware_type, capacity, memory)
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory

    @property
    def hardware_type(self):
        return self.__hardware_type

    @hardware_type.setter
    def hardware_type(self, type = 'Heavy'):
        self.__hardware_type = type
