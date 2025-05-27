from post import Post

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def create_post(self, content):
        return Post(content)