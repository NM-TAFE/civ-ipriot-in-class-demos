from post import Post

class TextPost(Post):
    def __init__(self):
        super().__init__()
        self.message = ""

    def get_message(self):
        return self.message

    def display(self):
        return f"""
        {self.username} posted: {self.message}
        at {self.timestamp}
        {self.likes} likes and {len(self.comments)} comments
        """


