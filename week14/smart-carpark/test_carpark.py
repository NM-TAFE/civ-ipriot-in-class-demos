import unittest

from car import Car
from car_park import CarPark
from display import Display
from sensor import Sensor

class TestCarPark(unittest.TestCase):
    def test_carpark_is_instantiated(self):
        self.assertIsInstance(CarPark(), CarPark)

    def test_car_is_instantiated(self):
        self.assertIsInstance(Car(), Car)

    def test_display_is_instantiated(self):
        self.assertIsInstance(Display(), Display)

    def test_sensor_is_instantiated(self):
        self.assertIsInstance(Sensor(), Sensor)