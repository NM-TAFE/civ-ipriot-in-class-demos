class Sensor:
    """
    Defines a car park sensor
    """
    def __init__(self, car_park):
        self.car_park = car_park


class EntrySensor(Sensor):
    """A sensor used to detect entries into the car park"""


class ExitSensor(Sensor):
    "A sensor that detects cars leaving the car park"

