from datetime import datetime

class PhotoPost:
    def __init__(self):
        self.username = None
        self.timestamp = datetime.now()
        self.likes = 0
        self.comments = []
        self.filename = ""
        self.caption = ""

    def add_comment(self, text):
        self.comments.append(text)

    def get_timestamp(self):
        return self.timestamp

    def get_filename(self):
        return self.filename

    def get_caption(self):
        return self.caption

    def like(self):
        self.likes += 1

    def display(self):
        return f"""
        {self.username} posted: <img src="{self.filename}" />
        {self.caption}
        at {self.timestamp}
        {self.likes} likes and {len(self.comments)} comments
        """

