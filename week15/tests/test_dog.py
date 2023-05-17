import unittest
from src.dog import Dog

class TestDog(unittest.TestCase):
    def setUp(self) -> None:
        self.name = "Fido"
        self.breed = "Labrador"
        self.dog = Dog(self.name, self.breed)

    def test_dog_bark_includes_name_of_dog(self):
        self.assertEqual(self.dog.bark(),
                          f"{self.name} says woof!")

    def test_dog_name_in_bark(self):
       self.assertIn(self.name,
                     self.dog.bark())