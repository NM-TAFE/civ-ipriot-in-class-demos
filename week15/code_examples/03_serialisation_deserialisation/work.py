import json
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
        self.validated_at = datetime.now().strftime("%Y-%m-%d")
        self.errors.clear()

        # Why are these all separate if-statements rather than one big if-elif block?
        # Consider the case where every single field is wrong.
        # It is more user-friendly for the developer to see a full list of everything which
        # must be fixed.
        if self.authors == None or len(self.authors) == 0:
            self.errors["authors"] = "Must include at least one author"

        if self.chapters == None or len(self.chapters) == 0:
            self.errors["chapters"] = "Must include at least one chapter"

        if self.title == None or len(self.title) == 0:
            self.errors["title"] = "Title must be at least one character"

        if self.summary == None or len(self.summary) == 0:
            self.errors["summary"] = "Summary must be at least one character"

        # This is a proxy for validity.  There are no errors, so it must be valid
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
            file_name = self.title.replace(" ", "_")
            with open(f"{file_name}.json", 'w', encoding="utf-8") as file:
                file.write(json.dumps(self.__dict__))
            return True
        else:
            return False

    @classmethod
    def load(cls, filename):
        "load from json file"
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
            data = json.loads(contents)
            print(data['title'])
            new_work = cls()
            new_work.title = data['title']
            new_work.summary = data['summary']
            new_work.chapters = data['chapters']
            new_work.authors = data['authors']
            return new_work

    def to_dict(self):
        return {
            "title": self.title,
            "summary": self.summary,
            "authors": self.authors,
            "chapters": self.chapters
        }
