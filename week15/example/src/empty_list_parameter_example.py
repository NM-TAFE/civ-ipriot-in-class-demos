import sys
sys.path.append("src")

"""
In the work for carpark, the directions say not to default an
argument to an empty list.  Here is a good example of why not.

What do you expect the print statements to say?
"""


class Test():
    def __init__(self, not_just_mutable_but_shared=[]):
        not_just_mutable_but_shared.append("?")
        self.shared = not_just_mutable_but_shared


if __name__ == "__main__":
    t1 = Test()
    print(t1.shared)

    t2 = Test()

    print("What do you expect each 'shared' value to be?")
    print(t1.shared)
    print(t2.shared)

    t2.shared.append("!")
    print("Well, this is probably not going to be ideal...")
    print(t1.shared)