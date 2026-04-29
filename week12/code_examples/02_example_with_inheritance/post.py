from datetime import datetime

class Post:
    def __init__(self):
        self.username = None
        self.timestamp = datetime.now()
        self.likes = 0
        self.comments = []

    def add_comment(self, text):
        self.comments.append(text)

    def get_timestamp(self):
        return self.timestamp

    def like(self):
        self.likes += 1

    def display(self):
        raise NotImplementedError

