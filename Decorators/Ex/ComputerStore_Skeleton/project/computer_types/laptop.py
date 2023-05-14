from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
import math

class Laptop(Computer):
    AVAILABLE_PROCESSOR = {
        'AMD Ryzen 7 5700G': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200
    }
    MAX_RAM = 64

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        self.__check_processor_is_available(processor, self.AVAILABLE_PROCESSOR)
        self.__check_ram_is_correct(ram, self.MAX_RAM)
        if not self.__check_ram_is_correct(ram, self.MAX_RAM):
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += self.__computer_price(ram, processor)
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {int(self.price)}$."


    def __check_processor_is_available(self, proc, available_proc):
        if proc not in available_proc.keys():
            raise ValueError(
                f"{proc} is not compatible with desktop computer {self.manufacturer} {self.model}!"
            )

    @staticmethod
    def __check_ram_is_correct(ram, max_ram):
        if ram == 0:
            return False
        return (ram & (ram - 1)) == 0 and ram <= max_ram


    def __computer_price(self,ram, processor):
        ram_price = math.log(ram, 2) * 100
        processor_price = 0
        for proc, value in self.AVAILABLE_PROCESSOR.items():
            if proc == processor:
                processor_price += value
        return ram_price + processor_price
