from contact import Contact

class EmailContact(Contact):
    def __init__(self):
        super().__init__()
        self.__email = ""

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if value.find("@") == -1:
            print("Email should contain an @ symbol")
        else:
            self.__email = value