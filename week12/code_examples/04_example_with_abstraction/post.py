from abc import ABC, abstractmethod
from datetime import datetime

class Post(ABC):
    def __init__(self):
        self.__username = None
        # In this example, you cannot set Timestamp.  It exists as it was created.
        self.__timestamp = datetime.now()
        self.__likes = 0
        self.__comments = []

    @property
    def comments(self):
        return self.__comments

    # Comments are special, because they are a list
    # We will not give it a generic "setter"
    def add_comment(self, text):
        self.__comments.append(text)

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 1:
            print("Username must be at least one character")
            return
        self.__username = value


    @property
    def likes(self):
        return self.__likes


    def like(self):
        self.__likes += 1


    @abstractmethod
    def display(self):
        raise NotImplementedError






