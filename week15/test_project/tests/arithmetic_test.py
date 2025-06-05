import unittest
from arithmetic import add

class ArithmeticTest(unittest.TestCase):
    def test_add_floats_correctly(self):
        # Of course we can assert that `add(2.0, 3.0)` is equivalent to `2.0 + 3.0`.  
        # But then your test will be "doing work".  Test code is untested code: make it as "stupid"
        # and straightforward as possible.
        self.assertAlmostEqual(add(2.0, 3.0), 5.0)
        self.assertAlmostEqual(add(8.6, 3.9), 12.5)

    # See how you can use _ to break up large numbers, improving human readability
    def test_add_integers_correctly(self):
        self.assertEqual(add(1,1), 2)
        self.assertEqual(add(99_999_999, 1), 100_000_000)

    def test_add_complex_numbers(self):
        self.assertEqual(add(1, 3+5j), 4+5j)
        self.assertEqual(add(1, 1+1j), 2+1j)

    def test_rejects_bad_values(self):
        with self.assertRaises(TypeError):
            add("hello", "world")
