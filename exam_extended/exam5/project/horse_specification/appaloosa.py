from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAXIMUM_HORSE_SPEED = 120
    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)


    def train(self):
        return self.speed * 2