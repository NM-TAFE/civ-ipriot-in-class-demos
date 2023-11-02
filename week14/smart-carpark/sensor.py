class Sensor:
    """
    Defines a car park sensor
    """
    def __init__(self, car_park):
        self.car_park = car_park

    def detect(self):
        """Triggered when a car enters the carpark"""
        print("Detection occurred")
        # TODO: send detection to car_park

class EntrySensor(Sensor):
    """A sensor used to detect entries into the car park"""
    # TODO: specialise the subclasses to deal with exit/entry


class ExitSensor(Sensor):
    """A sensor that detects cars leaving the car park"""

