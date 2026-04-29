from post import Post

class PhotoPost(Post):
    def __init__(self):
        super().__init__()
        self.filename = ""
        self.caption = ""

    def get_filename(self):
        return self.filename

    def get_caption(self):
        return self.caption

    def display(self):
        return f"""
        {self.username} posted: <img src="{self.filename}" />
        {self.caption}
        at {self.timestamp}
        {self.likes} likes and {len(self.comments)} comments
        """

