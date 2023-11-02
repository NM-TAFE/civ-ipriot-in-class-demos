class Car:
    """
    Tracks a car while it is in the car park
    """
    def __init__(self, plate = None):
        if plate:
            self.plate = plate
        else: # should raise exception or call the cops!
            print("Crazy illegal driver")
            self.plate = plate
        self._has_entered = False

    def entered_car_park(self):
        print("Car has entered")
        self._has_entered = True

    def exitted_car_park(self):
        print("Car has exitted")
        self._has_entered = False
