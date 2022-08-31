from animal import Animal, Bird


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    @property
    def alowed_feed(self):
        return ['meat']


    @property
    def weight_incrace(self):
        return 0.25


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    @property
    def alowed_feed(self):
        return ['meat','vegetables', 'fruits']


    @property
    def weight_incrace(self):
        return 0.35
