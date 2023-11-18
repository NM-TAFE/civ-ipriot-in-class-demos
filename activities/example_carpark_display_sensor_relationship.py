"""This code snippet shows us how we establish the relationship between a carpark and its components (sensors and displays). 
Because our sensors are not actual sensors (shock horror!), we have to do a little fudge to make sure that while incoming cars 
generate random plates, outgoing cars only generate plates of cars that are in the carpark.
"""
import random
from datetime import datetime
import time



## Helper functions           
def scroll_text(text, delay=0.1):
    for i in range(len(text) + 1):
        print(text[:i], end='\r', flush=True)
        time.sleep(delay)

def get_weather_data(location, min=0, max=42):
    '''Mock function to get weather data for a location. Returns a random number between min and max'''
    return random.randint(min, max)

def generate_bogus_plate(prefix="FAKE", sep='-'):
    '''Generate a random plate'''
    return prefix + sep + format(random.randint(0, 999), '03d')


## Example classes

# Note: these classes are not complete and are not intended to be used as-is.
# They are just here to illustrate the relationship between the components
# Read the instructions to see how to complete them.

class Carpark:
    def __init__(self, 
                 location,
                 sensors = None, 
                 displays = None,
                 plates = None):
        self.sensors = sensors or []
        self.displays = displays or []
        self.plates = plates or []
        self.location = location

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Invalid component type")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        else:
            self.displays.append(component)
            
    def add_car(self, plate):
        self.plates.append(plate)


    def remove_car(self, plate):
        self.plates.remove(plate)
        
    @property
    def available_bays(self):
        return 42 # see instructions to implement this correctly
    
    def update_displays(self):
        for display in self.displays:
            display.update({"bays": self.available_bays,
                            "temperature": get_weather_data(self.location)})
            
        
class Display:
    def __init__(self, carpark):
        self.carpark = carpark
        self.carpark.register(self)
        
    def update(self, data):
        for key, value in data.items():
            print("Time:", datetime.now().strftime("%H:%M"))  # print current time as hh:MM
            print(key, end=': ')
            scroll_text(str(value))
            print()

class Sensor:
    def __init__(self, carpark):
        self.carpark = carpark
        self.carpark.register(self)

    def _scan_plate(self):
        """Scans the plate using sophisticated number plate reading technology. 
        This proprietary technology combines neural networks, machine learning, and other buzzwords."""
        return generate_bogus_plate() 
    
    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_carpark(plate) # think about how this method is polymorphic (i.e. it behaves differently depending on sensor subclass)
        print("Detected vehicle with plate", plate)
        

class EntrySensor(Sensor):
    def update_carpark(self, plate):
        self.carpark.add_car(plate)

class ExitSensor(Sensor):
    def _scan_plate(self):
        # fudge to simulate only reading cars that exist
        # normally we would not need to override this method!
        return random.choice(self.carpark.plates)

    def update_carpark(self, plate):
        self.carpark.remove_car(plate)

