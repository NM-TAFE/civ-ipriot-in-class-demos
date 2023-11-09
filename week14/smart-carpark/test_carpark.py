import unittest

from car import Car
from car_park import CarPark
from display import Display
from sensor import Sensor

class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark('Moondalup CP',
                                      'Moondalup',
                                      42)
    def test_carpark_is_instantiated(self):
        self.assertIsInstance(self.car_park, CarPark)

    def test_car_is_instantiated(self):
        with self.assertRaises(TypeError):
            Car() # should not be able to create a car without a license
        self.assertIsInstance(Car('123-ABC'), Car)

    def test_display_is_instantiated(self):
        car_park = self.car_park
        self.assertIsInstance(Display(), Display)

    def test_sensor_is_instantiated(self):
        car_park = self.car_park
        self.assertIsInstance(Sensor(car_park), Sensor)
