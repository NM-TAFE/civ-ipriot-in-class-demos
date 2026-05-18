from polygon import Polygon

class RightTriangle(polygon):
    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
