from car import Car
import random
from abc import ABC, abstractmethod

class Sensor(ABC):
    """
    Defines a car park sensor
    """
    def __init__(self, car_park):
        self.car_park = car_park

    def _read_plate(self):
        return f"FAKE-{random.randint(0,1000):03}"

    def detect(self):
        """Triggered when a car enters the carpark"""
        car = Car(self._read_plate())
        self.update_car_park(car)

        print("Detection occurred")

    @abstractmethod
    def update_car_park(self, car):
        ...


class EntrySensor(Sensor):
    """A sensor used to detect entries into the car park"""
    def update_car_park(self, car):
        self.car_park.add_car(car)


class ExitSensor(Sensor):
    """A sensor that detects cars leaving the car park"""
    def update_car_park(self, car):
        self.car_park.remove_car(car)
