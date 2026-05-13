from post import Post

class PhotoPost(Post):
    def __init__(self):
        super().__init__()
        self.__filename = ""
        self.__caption = ""

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, value):
        if not value or len(value) < 1:
            print("Filename must be at least one character")
            return
        self.__filename = value

    @property
    def caption(self):
        return self.__caption

    @caption.setter
    def caption(self, value):
        if not value or len(value) < 1:
            print("Caption must be at least one character")
            return
        self.__caption = value

    def display(self):
        return f"""
        {self.username} posted: <img src="{self.filename}" />
        {self.caption}
        at {self.timestamp}
        {self.likes} likes and {len(self.comments)} comments
        """


