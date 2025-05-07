# As an example of polymorphism -- these 3 unrelated classes
# have "an interface" in common, and so can be called the
# same way.
class Bike():
    def __init__(self):
        self.number_of_wheels = 2

class Car():
    def __init__(self):
        self.number_of_wheels = 4

class Rollerblades():
    def __init__(self):
        self.number_of_wheels = 8

bike = Bike()
car = Car()
rollerblades = Rollerblades()

for device in [bike, car, rollerblades]:
    print(device.number_of_wheels)