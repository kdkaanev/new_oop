from project.computer_types.computer import Computer


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
        self.__check_processor_is_available(processor)
        self.__check_ram_is_correct(ram)


    def __check_processor_is_available(self, proc):
        if proc not in self.AVAILABLE_PROCESSOR.keys():
            raise ValueError(
                f"{self.processor} is not compatible with desktop computer {self.manufacturer} {self.model}!"
                )

    def __check_ram_is_correct(self, ram):
        if ram == 0:
            return False
        return (ram & (ram - 1)) == 0 and ram <= self.MAX_RAM
