from contact import Contact

class EmailContact(Contact):
    def __init__(self):
        self.__email = ""

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value:str):
        if value.find("@") == -1:
            print("Email should contain an @ symbol")
            return
        self.__email = value