from cat import Cat
import unittest

class TestCat(unittest.TestCase):
    def setUp(self):
        self.c = Cat("K", "T")


    def test_cat_has_a_name(self):
        self.assertEqual(self.c.name, "J")
        # arrange

    def test_cat_has_a_coat(self):
        ...

    def test_cat_meows_when_it_speaks(self):
        self.assertTrue(hasattr(Cat, "speak"))

if __name__ == '__main__':
    unittest.main()