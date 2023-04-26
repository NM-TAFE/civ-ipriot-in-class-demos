from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius


    def area(self): #calculate_area?
        return pi * self.radius**2 # print(...)

class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2

def return_the_larger_shape_by_area(shape1, shape2):
    pass

circle = Circle(5)
square = Square(5)
print(return_the_larger_shape_by_area(circle, square)) #return circle

circle = Circle(5)

