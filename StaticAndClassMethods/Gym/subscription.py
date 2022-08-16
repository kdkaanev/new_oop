from turtle import st


class Subscription:
    id = 1

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_next_id():
        Subscription.id += 1
        return Subscription.id

    def __repr__(self):
        return f"Trainer <{id}> {self.name}"