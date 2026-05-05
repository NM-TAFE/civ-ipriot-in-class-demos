from datetime import datetime
import time_of_day
# Snip
import unittest

class TestTimeOfDay(unittest.TestCase):
    def test_6am_is_morning(self):
        actual = time_of_day.humanise(self.__time_by_hour(6))
        self.assertEqual(actual, "morning")

    def test_959am_is_morning(self):
        actual = time_of_day.humanise(self.__time_by_hour(9, cusp=True))
        self.assertEqual(actual, "morning")

    def test_10am_is_day(self):
        actual = time_of_day.humanise(self.__time_by_hour(10))
        self.assertEqual(actual, "day")

    def test_1359pm_is_day(self):
        actual = time_of_day.humanise(self.__time_by_hour(13, cusp=True))
        self.assertEqual(actual, "day")

    def test_14pm_is_afternoon(self):
        actual = time_of_day.humanise(self.__time_by_hour(14))
        self.assertEqual(actual, "afternoon")

    def test_1759pm_is_afternoon(self):
        actual = time_of_day.humanise(self.__time_by_hour(14))
        self.assertEqual(actual, "afternoon")

    def test_18pm_is_evening(self):
        actual = time_of_day.humanise(self.__time_by_hour(18))
        self.assertEqual(actual, "evening")

    def test_2159pm_is_afternoon(self):
        actual = time_of_day.humanise(self.__time_by_hour(21, cusp=True))
        self.assertEqual(actual, "evening")

    def test_22pm_is_night(self):
        actual = time_of_day.humanise(self.__time_by_hour(22))
        self.assertEqual(actual, "night")

    def test_559am_is_night(self):
        actual = time_of_day.humanise(self.__time_by_hour(5, cusp=True))
        self.assertEqual(actual, "night")

    # This is *untested* code.
    # It is up to you to decide how much logic you want to include
    # But less is better.
    def __time_by_hour(self, hour, cusp=False):
        minutes = 59 if cusp else 0
        return  datetime(2026, 1, 1, hour, minutes)