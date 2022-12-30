from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    GINGERBREAD_PORTION = 200
    def __init__(self, name: str, portion: int, price: float):
        super().__init__(name, portion, price)
        self.price = price
        self.portion = self.GINGERBREAD_PORTION
        self.name = name

    def details(self):
        return f"Gingerbread {self.name}: {self.GINGERBREAD_PORTION}g - {self.price:.2f}lv."

