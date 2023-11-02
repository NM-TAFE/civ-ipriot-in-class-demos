from sensor import EntrySensor, ExitSensor
from car_park import CarPark
from display import Display
# Sequence:
# car enters:
car_park = CarPark('A', 'B', 100)
car_park.register_display(Display())
entry_sensor = EntrySensor(car_park)
exit_sensor = ExitSensor(car_park)

entry_sensor.detect()

# car leaves...
# sensor reads plate
# sensor sends info (exit) to car_park
