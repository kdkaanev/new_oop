from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop
from project.computer_types.computer import Computer


class ComputerStoreApp:
    VALID_TYPES = {
        "Laptop": Laptop,
        "Desktop Computer": DesktopComputer
    }

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_TYPES.keys():
            raise ValueError(f"{type_computer} is not a valid type computer!")
        for comp_type, comp in self.VALID_TYPES.items():
            if comp_type == type_computer:
                computer = comp(manufacturer, model)
                computer.processor = processor
                computer.ram = ram
                self.warehouse.append(computer)
                return computer.configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for comp in self.warehouse:
            if comp.price <= client_budget and comp.processor == wanted_processor and comp.ram >= wanted_ram:
               self.profits += (client_budget - comp.price)
               return f"{comp. __repr__():} sold for {client_budget}$."
            else:
                raise Exception("Sorry, we don't have a computer for you.")
