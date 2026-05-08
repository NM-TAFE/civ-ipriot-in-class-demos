from meeting import Meeting
from loadable import Loadable

class Conference(Meeting, Loadable):
    def __init__(self, attendance_mode, start_date, end_date, subject):
        super().__init__(attendance_mode, start_date, end_date)
        self.subject = subject

    def  __str__(self):
        base_string = super().__str__()
        return base_string + " " + self.subject

    @classmethod
    def load(cls, object_dictionary):
        return cls(
            attendance_mode=object_dictionary.get("attendance_mode"),
            start_date=object_dictionary.get("start_date"),
            end_date=object_dictionary.get("end_date"),
            subject=object_dictionary.get("subject")
        )