class Contact:
    def __init__(self):
        self.__name = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) < 1:
            print("Error: The contact's name should be at least 1 character")
            return

        if len(value) < 2:
            print("Warning: did you mean to enter such a short name?")

        self.__name = value
