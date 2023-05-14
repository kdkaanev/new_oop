from project.computer_types.computer import Computer
import math


class DesktopComputer(Computer):
    AVAILABLE_PROCESSOR = {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5-12600K': 600,
        'Apple M1 Max': 1800
    }
    MAX_RAM = 128

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        self.__check_processor_is_available(processor, self.AVAILABLE_PROCESSOR)
        self.__check_ram_is_correct(ram)
        if not self.__check_ram_is_correct(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += self.__computer_price(ram, processor)
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {int(self.price)}$."

    def __check_ram_is_correct(self, ram):
        if ram == 0:
            return False
        return (ram & (ram - 1)) == 0 and ram <= self.MAX_RAM

    def __computer_price(self, ram, processor):
        ram_price = math.log(ram, 2) * 100
        processor_price = 0
        for proc, value in self.AVAILABLE_PROCESSOR.items():
            if proc == processor:
                processor_price += value
        return ram_price + processor_price
