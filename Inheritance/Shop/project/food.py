from project.product import Product


class Food(Product):
    QUANTITY = 15

    def __init__(self, name: str, quantity=None):
        super().__init__(name, quantity)
        self.quantity = quantity if quantity else self.QUANTITY
