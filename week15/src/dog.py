
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"



if __name__ == '__not_main__':
    fido = Dog("Fido", "Labrador") # Fido says woof
    print(fido.bark())
    assert "Fido says woof!     " == fido.bark()