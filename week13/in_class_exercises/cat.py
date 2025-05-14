# Checklist:
# - File with same name as class (lower_snake)
# - Names are PEP8
#  - Private attributes/methods start with '_'
# - Include implicit behaviours (e.g. self)
# - Otherwise stick to spec!






class Cat:
    def __init__(self, is_cute: bool, age: int, coat: str):
        self._is_cute = is_cute
        self._age = age
        self._coat = coat

    def purr(self) -> None:
        print(f"Purr")

    def meow(self):
        print("Meow")

    def eat(self):
        print("Gobble gobble")