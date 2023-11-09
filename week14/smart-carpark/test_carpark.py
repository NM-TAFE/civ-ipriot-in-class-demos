import unittest
from car_park import CarPark
from display import Display
from sensor import Sensor, EntrySensor, ExitSensor

class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark('Moondalup CP',
                                      'Moondalup',
                                      42)
    def test_carpark_is_instantiated(self):
        self.assertIsInstance(self.car_park, CarPark)


    def test_display_is_instantiated(self):
        car_park = self.car_park
        self.assertIsInstance(Display(), Display)

    def test_sensor_is_instantiated(self):
        car_park = self.car_park
        self.assertIsInstance(EntrySensor(car_park), Sensor)
        self.assertIsInstance(ExitSensor(car_park), Sensor)
