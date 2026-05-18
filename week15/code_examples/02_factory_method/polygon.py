from abc import ABC, abstractmethod

from quadrilateral import Quadrilateral
from circle import Circle
from right_triangle import RightTriangle


class Polygon(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        raise NotImplementedError

    @classmethod
    def make_shape(cls, sides):
        print("Warn: Shape is being created with default dimensions")

        if sides == 1 or sides == 0 or sides == 'infinite':
            return Circle()
        if sides < 3:
            print("Warn! This seems awfully theoretical, are you okay?")
            return cls()
        if sides == 3:
            return Triangle()
        if sides == 4:
            return Quadrilateral()
        if sides > 4:
            print("Sorry, not implemented yet")
            return cls()