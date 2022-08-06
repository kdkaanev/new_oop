from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self,product: Product):
        self.products.append(product)

    def find(self, product_name):
        return product_name

    def remove(self, product_name):
        self.products.remove(product_name)

    def __repr__(self):
        pass
