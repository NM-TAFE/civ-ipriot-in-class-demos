"""
These are fake unit tests.
They do assertions, and are called by 'the runner', run_all_tests
They do not scale well and contain a lot of boilerplate.

These are not for copying, they're for getting an idea across.

Go look at test_time_of_day to see the use of unittest
"""
from time_of_day import humanise
from datetime import datetime


def test_6am_is_morning():
    six_am = datetime(2026, 1, 1, 6, 0) # Arrange
    actual = humanise(six_am) # Act
    print(f"Expected 'morning', Got: '{actual}'") # Assert


def test_10am_is_day():
    ten_am = datetime(2026, 1, 1, 10, 0)
    actual = humanise(ten_am)
    assert actual == "Day"
    print("10am is day")


def run_all_tests():
    passing = True
    for each_test in [test_6am_is_morning, test_10am_is_day]:
        try:
            each_test()
        except AssertionError:
            print(f"{each_test.__name__} failed")
            passing = False

    if passing:
        print("All tests passed")
    else:
        print("Tests failed")
        exit(1)


if __name__ == "__main__":
    run_all_tests()