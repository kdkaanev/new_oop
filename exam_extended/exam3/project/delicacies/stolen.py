from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    STOLEN_PORTION = 250
    def __init__(self, name: str, portion: int, price: float):
        super().__init__(name, portion, price)
        self.price = price
        self.portion = self.STOLEN_PORTION
        self.name = name

    def details(self):
        return f"Gingerbread {self.name}: {self.STOLEN_PORTION}g - {self.price:.2f}lv."