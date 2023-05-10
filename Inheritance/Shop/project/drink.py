from project.product import Product


class Drink(Product):
    QUANTITY = 10

    def __init__(self, name: str, quantity=None):
        super().__init__(name, quantity)
        self.quantity = quantity if quantity else self.QUANTITY
