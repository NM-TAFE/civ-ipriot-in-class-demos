class NotSelf:
    def __init__(x, name):
        x.name = name

    def speak(y):
        print(f"{y.name} speaks!")


z = NotSelf("Fred")
z.speak()