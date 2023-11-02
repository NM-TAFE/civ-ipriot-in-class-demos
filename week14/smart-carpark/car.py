class Car:
    """
    Tracks a car while it is in the car park
    """
    def __init__(self, plate):
        self.plate = plate
        self._has_entered = False

    def entered_car_park(self):
        print("Car has entered")
        self._has_entered = True

    def exitted_car_park(self):
        print("Car has exitted")
        self._has_entered = False
