from project.meals.meal import Meal


class Dessert(Meal):
    DEFAULT_QUANTITY = 30

    def __init__(self, name: str, price: float, quantity: int = None):
        self.quantity = quantity if quantity else self.DEFAULT_QUANTITY
        super().__init__(name, price, quantity)

    def details(self):
        return f"Dessert {self.name}: {self.price:2f}lv/piece"



