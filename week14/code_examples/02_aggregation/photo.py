from attachment import Attachment

class Photo(Attachment):
    def __init__(self):
        self.__filepath = None
        self.alt_text = None

    @property
    def type(self):
        """
        Interestingly, this is kind of unnecessary.  The 'easy way'
        is a little magical though, so let's stick with this.
        (__class__.__name__)
        """
        return "photo"

    @property
    def filepath(self):
        return self.__filepath

    @filepath.setter
    def filepath(self, value):
        if "/" not in value: # very unix, much slash
            print("Not a valid path")
            return

        self.__filepath = value

    def __str__(self):
        return f"!()[{self.filepath}]\nalt: {self.alt_text}"


