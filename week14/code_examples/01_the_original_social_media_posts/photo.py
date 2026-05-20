class Photo:
    def __init__(self, filename="", content="", alt_text=""):
        self.filename = filename
        self.content = content
        self.alt_text = alt_text

    def __str__(self):
        return f"{self.filename}, {self.alt_text}"
