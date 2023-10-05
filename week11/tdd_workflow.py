# Outlines the code for the TDD workflow in the following video:
# https://www.youtube.com/watch?v=ibVSPVz2LAA (Python TDD Workflow - Unit Testing Code Example for Beginners by Python Simplified)
"""Demonstrates TDD workflow for a simple shift cipher. 
Note that there are some practices that we will contrast with:
Use more meaningful names; don't replicate a function's logic in the test case."""
import unittest

class TestEncryption(unittest.TestCase):
    def test_message_exists(self):
        self.assertIsNotNone(self.my_message)

# Code to be updated in class