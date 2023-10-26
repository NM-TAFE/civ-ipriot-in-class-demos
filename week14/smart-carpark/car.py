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
