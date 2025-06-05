import unittest
from cat import Cat

class CatTest(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_ex(self):
        with self.assertRaises(TypeError):
            Cat("Spots", 9001)