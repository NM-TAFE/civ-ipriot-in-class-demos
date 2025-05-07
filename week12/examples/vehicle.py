class Vehicle():
    def go_somewhere(self):
        print("===>")

class Car(Vehicle):
    def honk(self):
        print("honk")


# Where do you expect the following to fail?
car = Car()
car.go_somewhere()
car.honk()

vehicle = Vehicle()
vehicle.go_somewhere()
vehicle.honk()