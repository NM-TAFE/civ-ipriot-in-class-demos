import time

class Display:
    """
    Displays information to drivers about the availability of bays
    as well as the current weather conditions.
    """
    def __init__(self, car_park):
        self.car_park = car_park
        self.temperature = None
        self.available_bays = None
        self.show_full = False
        self.banner = None

    def display_board(self):
        print("Displaying bays and temp on the board")
        # TODO: implement the board


    def check_for_updates_forever(self):
        while True:
            time.sleep(2)
            print("Checking for updates...")
            # TODO: implement check
            # TODO: call display_board

