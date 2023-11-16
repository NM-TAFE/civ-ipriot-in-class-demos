"""This code snippet shows us how we establish the  relationship
between a carpark and its components (sensors and displays).Because our sensors are not actual sensors (shock horror!),
we have to do a little fudge to make sure that while
incoming cars generate random plates, outgoing cars only generate plates
of cars that are in the carpark.
"""
import random
class Carpark:
    def __init__(self, sensors = None, displays = None):
        self.sensors = sensors or []
        self.displays = displays or []
        self.plates = ["A", "B", "C"]

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Invalid component type")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        else:
            self.displays.append(component)


    def remove_car(self, plate):
        self.plates.remove(plate)
class Display:
    def __init(self, carpark):
        self.carpark = carpark
        self.carpark.register(self)

class Sensor:
    def __init(self, carpark):
        self.carpark = carpark
        self.carpark.register(self)

    def _read_plate(self):
        return random.choice("ABCDEFGHIJK")

class EntrySensor(Sensor):
    pass

class ExitSensor(Sensor):
    def _read_plate(self):
        # fudge to simulate only reading cars that exist
        return random.choice(self.carpark.plates)

    def detect_car(self):
        plate = self._read_plate()
        self.carpark.remove_car(plate)

