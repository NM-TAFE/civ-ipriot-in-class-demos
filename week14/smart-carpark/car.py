class Car:
    def __init__(self, plate = None):
        if plate:
            self.plate = plate
        else:
            print("Crazy illegal driver")
            self.plate = plate
