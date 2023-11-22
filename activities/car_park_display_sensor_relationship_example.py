"""This code snippet shows us how we establish the relationship between a car park and its components (sensors and displays). 
Because our sensors are not actual sensors (shock horror!), we have to do a little fudge to make sure that while incoming cars 
generate random plates, outgoing cars only generate plates of cars that are in the car park.
"""
import random
from datetime import datetime
import time



## Helper functions           
def scroll_text(text, delay=0.2):
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

class CarPark:
    def __init__(self, 
                 location,
                 sensors = None, 
                 displays = None,
                 plates = None):
        self.sensors = sensors or []
        self.displays = displays or []
        self.plates = plates or []
        self.location = location
        self.total_bays = 10

    def register(self, component): # notice that "component" suggests that we may want a superclass for Sensor and Display
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Invalid component type")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        else:
            self.displays.append(component)
            
    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()


    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        
    @property
    def available_bays(self):
        return max(0, self.total_bays - len(self.plates)) # see instructions to implement this correctly
    
    def update_displays(self):
        for display in self.displays:
            display.update({"bays": self.available_bays,
                            "temperature": get_weather_data(self.location)})
            
        
class Display:
    def __init__(self, car_park):
        self.car_park = car_park
        self.car_park.register(self)
        
    def update(self, data):
        print("Time:", datetime.now().strftime("%H:%M"))  # print current time as hh:MM
        for key, value in data.items():
            print(key, value, sep=': ')
            time.sleep(0.1)
        print()

class Sensor:
    def __init__(self, car_park):
        self.car_park = car_park
        self.car_park.register(self)

    def _scan_plate(self):
        """Scans the plate using sophisticated number plate reading technology. 
        This proprietary technology combines neural networks, machine learning, and other buzzwords."""
        return generate_bogus_plate() 
    
    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate) # think about how this method is polymorphic (i.e. it behaves differently depending on sensor subclass)
        print("Detected vehicle with plate", plate)
        

class EntrySensor(Sensor):
    def update_car_park(self, plate):
        print("🚘 entered car park")
        self.car_park.add_car(plate)

class ExitSensor(Sensor):
    def _scan_plate(self):
        # fudge to simulate only reading cars that exist
        # normally we would not need to override this method!
        return random.choice(self.car_park.plates)

    def update_car_park(self, plate):
        print("🚗 exited car park")
        self.car_park.remove_car(plate)

def main():
    car_park = CarPark("Perth")
    EntrySensor(car_park) # notice how the registration is **implicit** in the constructor
    ExitSensor(car_park) # in our final version we will make this explicit
    Display(car_park)

    while True:
        # You don't have to worry about this code too much it is just to simulate cars entering and exiting
        occupancy_ratio = len(car_park.plates) / car_park.total_bays
        entry_probability = max(0.1, 1 - occupancy_ratio)  # Lower probability if car_park is fuller
        exit_probability = max(0.1, occupancy_ratio - 1)  # Higher probability if car_park is fuller

        for sensor in car_park.sensors:
            time.sleep(1)
            if isinstance(sensor, EntrySensor):
                if random.random() < entry_probability:
                    sensor.detect_vehicle()
            elif isinstance(sensor, ExitSensor) and len(car_park.plates) > 0:
                if random.random() < exit_probability:
                    sensor.detect_vehicle()  

if __name__ == "__main__":
    main()