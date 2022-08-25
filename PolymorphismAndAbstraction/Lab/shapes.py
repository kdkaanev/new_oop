from abc import abstractmethod


from abc import ABC
from math import pi

class Shapes(ABC):
    pass

    @abstractmethod
    def  calculate_area():
        pass


    @abstractmethod
    def  calculate_perimeter():
        pass



class Circle(Shapes):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius * self.radius
    
    def calculate_perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shapes):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return (self.width + self.height) * 2


rectangle = Rectangle(10, 20)

print(rectangle.calculate_area())

print(rectangle.calculate_perimeter()) 
        