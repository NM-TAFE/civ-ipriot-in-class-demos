"""
Step one, run this code with
python -m unittest
"""
"""
New convention: we prefer to import standard library functions at the top
and our own code lower down.

See how we first import unittest, and then import calculator.
"""
import unittest

from silly_calculator import SillyCalculator

class TestSillyCalculator(unittest.TestCase):
    # ========= Add Tests =========
    def test_add_1_1_returns_2(self):
        calculator = SillyCalculator(1, 1)
        self.assertEqual(calculator.add(), 2)


    def test_add_floats_works(self):
        calculator = SillyCalculator(8.32, 16.0)
        self.assertEqual(calculator.add(), 24.32)

    # Add a unit test that shows that add should return "I don't feel like it"
    # if and only if the first and second numbers are both 9.


    # ========= Subtract Tests =========
    # Add a unit test that checks that negative numbers can be returned


    # ========= Multiply Tests =========
    def test_multiply_4_8_returns_32(self):
        calculator = SillyCalculator(4, 8)
        self.assertEqual(calculator.multiply(), 32)


    # ========= Divide Tests =========
    def test_divide_by_zero_raises_error(self):
        calculator = SillyCalculator(1, 0)
        # Extension:
        # Add a test here that checks that calling 'divide'
        # triggers an error.
        # You will need to research "self.assertRaises()"
        # assertRaises() must be used as a 'context', using 'with'.

    # ========= Exponent Tests =========
    def test_exponent_2_4_returns_16(self):
        calculator = SillyCalculator(2, 4)
        self.assertEqual(calculator.exponent(), 16)