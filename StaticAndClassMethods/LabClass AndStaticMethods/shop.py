class Shop:

    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if len(self.items) == self.capacity:
            return "Not enough capacity in the shop"
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1

    def remove_item(self, item_name, amount):
        pass

