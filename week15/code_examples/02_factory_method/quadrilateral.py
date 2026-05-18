from polygon import Polygon

class Quadrilateral(Polygon):
    def __init__(self, height=2, width=2):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return self.height * 2 + self.width * 2
