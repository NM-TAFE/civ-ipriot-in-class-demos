# Outlines the code for the TDD workflow in the following video:
# https://www.youtube.com/watch?v=ibVSPVz2LAA (Python TDD Workflow - Unit Testing Code Example for Beginners by Python Simplified)
"""Demonstrates TDD workflow for a simple shift cipher. 
Note that there are some practices that we will contrast with:
Use more meaningful names; don't replicate a function's logic in the test case."""
import unittest

def encrypt(message):
    return message

class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.my_message = "banana"
    def test_message_exists(self):
        self.assertIsNotNone(self.my_message)

    def test_input_type_is_string(self):
        self.assertIsInstance(self.my_message, str)

    def test_encryption_returns_a_value(self):
        self.assertIsNotNone(encrypt(self.my_message))

    def test_encryption_returns_a_value_of_the_same_length(self):
        self.assertEqual(len(self.my_message),
                         len(encrypt(self.my_message)))

    def test_input_message_not_equal_output_message(self):
        self.assertNotEqual(self.my_message, encrypt(self.my_message))

if __name__ == '__main__':
    unittest.main()
# Code to be updated in class