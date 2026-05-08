from meeting import Meeting
from loadable import Loadable

class Hackathon(Meeting, Loadable):
    def __init__(self, attendance_mode, start_date, end_date, theme, description):
        super().__init__(attendance_mode, start_date, end_date)
        self.theme = theme
        self.description = description

    @classmethod
    def load(cls, object_dictionary):
        return cls(
            attendance_mode=object_dictionary.get("attendance_mode"),
            start_date=object_dictionary.get("start_date"),
            end_date=object_dictionary.get("end_date"),
            theme=object_dictionary.get("theme"),
            description=object_dictionary.get("description")
        )