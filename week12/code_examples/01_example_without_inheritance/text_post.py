from datetime import datetime

"""
I opted to make all attributes public to keep this class
short, for demonstration.
It would be better to make those private, and have "getters"
and "setters".

The way Python handles "getters" and "setters" is beyond this
class, but may be taught in a later class in your Cert IV.
"""
class TextPost:
    def __init__(self):
        self.username = None
        self.timestamp = datetime.now()
        self.likes = 0
        self.comments = []
        self.message = ""

    def add_comment(self, text):
        self.comments.append(text)

    def get_timestamp(self):
        return self.timestamp

    def get_message(self):
        return self.message

    def like(self):
        self.likes += 1

    def display(self):
        return f"""
        {self.username} posted: {self.message}
        at {self.timestamp}
        {self.likes} likes and {len(self.comments)} comments
        """


