from datetime import datetime
from attachment import Attachment

class Post():
    def __init__(self):
        self.__username = None
        # In this example, you cannot set Timestamp.  It exists as it was created.
        self.__timestamp = datetime.now()
        self.__likes = 0
        self.__comments = []
        self.__attachments = []
        self.message = None # Message can be public!

    @property
    def comments(self):
        return self.__comments

    @property
    def attachments(self):
        return self.__attachments

    def add_attachment(self, attachment):
        # This is a bit special:
        # __class__ is a dunder method that returns the Class of an object
        # Eg, a comment object for a specific comment would return a Comment class
        # (if it was implemented this way)
        if issubclass(attachment.__class__, Attachment):
            self.__attachments.append(attachment)
        else:
            print("Hey, that wasn't a real attachement!!")

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

    def serialise_attachments(self):
        if not self.attachments or len(self.attachments) == 0:
            return ""

        accumulated_attachments = ""
        count = 1
        for attachment in self.attachments:
            accumulated_attachments += f"Attachment #{count}\n"
            accumulated_attachments += str(attachment)
            accumulated_attachments += "\n"
            count += 1
        return accumulated_attachments



    def display(self):
        # What is with this indentation? """ triple quote strings are literal
        # And I don't want all that space on the left, so I had to push it sideways.
        output = \
f"""
========================================================================
{self.username} posted on {self.timestamp}
{self.likes} likes and {len(self.comments)} comments
========================================================================
{self.message}
---
{self.serialise_attachments()}
"""
        print(output)






