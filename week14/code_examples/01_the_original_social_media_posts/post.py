from datetime import datetime
from photo import Photo

class Post():
    def __init__(self):
        self.__username = None
        # In this example, you cannot set Timestamp.  It exists as it was created.
        self.__timestamp = datetime.now()
        self.__likes = 0
        self.__comments = []
        self.message = ""
        self.photos = []

    def add_photo(self, photo):
        if not isinstance(photo, Photo):
            print("Can only attach photos")
            return

        self.photos.append(photo)


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


    def serialised_photos(self):
        output = ""
        for photo in self.photos:
            output += str(photo)
            output += "\n"
        return output

    def display(self):
        return f"""
        {self.username} posted: {self.message}
        at {self.timestamp}
        {self.likes} likes and {len(self.comments)} comments
        {self.serialised_photos()}
        """






