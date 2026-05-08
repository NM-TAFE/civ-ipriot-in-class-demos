from datetime import datetime

class Work:
    """
    Represents a work to be stored in the system.
    Typically a piece of written text.
    """
    def __init__(self):
        self.authors = []
        self.chapters = []
        self.title = ""
        self.summary = ""

        self.errors = {}
        self.validated_at = None


    def is_valid(self):
        self.errors.clear()

        if len(self.chapters) < 1:
            self.errors['chapters'] = "Should have at least one chapter"

        if self.title is None or len(self.title) < 1:
            self.errors['title'] = "Title should have at least one character"

        return len(self.errors) == 0



    def __str__(self):
        return f"""
        {self.title}
        Written by: {"; ".join(self.authors)}
        Summary: {self.summary}
        Chapter Count: { len(self.chapters) }
        """

    def save(self):
        """
        Returns true if the record is saved successfully.
        If save fails, check self.errors for fixes.
        """
        currently_valid = self.is_valid()
        if currently_valid:
            "Do your save logic -- we'll cover this in serialisation-deserialisation"
            return True
        else:
            return False

    def add_chapter(self, text):
        self.chapters.append(text)