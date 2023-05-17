import unittest
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

class TestDog(unittest.TestCase):
    def setUp(self) -> None:
        self.name = "Fido"
        self.breed = "Labrador"
        self.dog = Dog(self.name, self.breed)

    def test_dog_bark_includes_name_of_dog(self):
        self.assertEquals(self.dog.bark(),
                          f"{self.name} says woof!")

    def test_dog_name_in_bark(self):
       self.assertIn(self.name,
                     self.dog.bark())

if __name__ == '__not_main__':
    fido = Dog("Fido", "Labrador") # Fido says woof
    print(fido.bark())
    assert "Fido says woof!     " == fido.bark()