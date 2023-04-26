from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    pass
tri = Triangle()
print('Triangle area:', tri.area())

class Circle(Shape):
    def __init__(self, name, radius):
        self.name = name
        self.radius = radius


    def area(self): #calculate_area?
        return pi * self.radius**2 # print(...)

class Square(Shape):
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def area(self):
        return self.length**2

def return_the_larger_shape_by_area(shape1, shape2):
    if shape1.area() > shape2.area():
        return shape1
    else:
        return shape2

circle = Circle('circle', 5)
square = Square('square', 5)
print(return_the_larger_shape_by_area(circle, square)) #return circle

Shape()

