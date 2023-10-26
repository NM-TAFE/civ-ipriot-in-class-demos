class Display:
    """
    Displays information to drivers about the availability of bays
    as well as the current weather conditions.
    """
    def __init__(self):
        self.temperature = None
        self.available_bays = None
        self.show_full = False
        self.banner = None

