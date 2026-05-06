from contact import Contact

class PhoneContact(Contact):
    """
    Remember: Phone numbers are not numbers.  They are strings
    that happen to contain digits.
    """
    def __init__(self):
        self.__phone_number = None
        self.__area_code = None

    @property
    def full_phone_number(self):
        return f"{self.__area_code}-{self.__phone_number}"

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        value = value.strip()
        if len(value) == 0:
            return

        if not value.isdigit():
            return

        self.__phone_number = value

    @property
    def area_code(self):
        return self.__area_code

    @area_code.setter
    def area_code(self, value):
        value = value.strip()
        if len(value) == 0:
            return

        if not value.isdigit():
            return
        # Perhaps you could check the validity of the value here?
        self.__area_code = value