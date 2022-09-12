import abc


class Shapes(abc.ABC):
    @abc.abstractmethod
    def calc_area(self):
        pass


class Huj(Shapes):
    def __init__(self, big):
        self.big = big

    def calc_area(self):
        return self.big * 3


class Rectangle(Shapes):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


class AreaCalculator:

    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calc_area()

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6), Huj(4)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
