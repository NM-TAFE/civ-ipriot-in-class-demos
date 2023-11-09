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
        plate = self._read_plate()
        self.update_car_park(plate)

        print("Detection occurred")

    @abstractmethod
    def update_car_park(self, plate):
        ...


class EntrySensor(Sensor):
    """A sensor used to detect entries into the car park"""
    def update_car_park(self, plate):
        self.car_park.add_car(plate)


class ExitSensor(Sensor):
    """A sensor that detects cars leaving the car park"""
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
