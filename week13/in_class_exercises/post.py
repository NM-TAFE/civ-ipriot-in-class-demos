from datetime import datetime
class Post:
    def __init__(self, content):
        self.content = content
        self.timestamp = datetime.now()


    def display_post(self):
        print(f"Post: {self.content}\n"
                f"At: {self.timestamp:%Y-%m-%d %H:%M}")
