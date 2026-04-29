from post import Post

class TextPost(Post):
    def __init__(self):
        super().__init__()
        self.__message = ""

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value

    def display(self):
        return f"""
        {self.username} posted: {self.message}
        at {self.timestamp}
        {self.likes} likes and {len(self.comments)} comments
        """



class TextPost(Post):
    def __init__(self):
        super().__init__()
        self.__message = ""

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value