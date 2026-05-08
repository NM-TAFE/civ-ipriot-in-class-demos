from abc import ABC

class Meeting(ABC):
    def __init__(self, attendance_mode, start_date, end_date):
        self.attendance_mode = attendance_mode
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"A {self.__class__.__name__}: {self.attendance_mode}." \
            + f"Starts: {self.start_date}, ends: {self.end_date}"