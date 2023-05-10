from project.animals.animal import Bird


class Owl(Bird):
    def __init__(self, wing_size: float, name: str, weight: float):
        super().__init__(wing_size, name, weight)

    def make_sound(self):
        return "Hoot Hoot"

class Hen(Bird):
    def __init__(self, wing_size: float, name: str, weight: float):
        super().__init__(wing_size, name, weight)

    def make_sound(self):
        return 'Cluck'