from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_HORSE_SPEED = 140

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        return self.speed * 3