from meals.meal import Meal


class Dessert(Meal):
    def __init__(self, name: str, price: float, quantity=30):
        super().__init__(name, price, quantity)
        self.name = name
        self.price = price
        self.quantity = quantity

    def details(self):
        return f"Dessert {self.name}: {self.price:.2f}lv/piece"

