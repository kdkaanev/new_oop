from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    BASE_WEIGHT = 7

    def __init__(self, name: str, kind: str, price: float, weight: int = None):
        super().__init__(name, kind, price, weight)
        self.weight = weight if weight else self.BASE_WEIGHT

    def eating(self):
        self.weight += 1
