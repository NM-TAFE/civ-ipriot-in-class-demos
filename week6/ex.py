class HelloContext:
    def __init__(self):
        print("In init")
    def __enter__(self):
        print("entering context")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exiting context")
        print(f"{exc_type = }, {exc_val = }, {exc_tb = }")


with HelloContext():
    ...
