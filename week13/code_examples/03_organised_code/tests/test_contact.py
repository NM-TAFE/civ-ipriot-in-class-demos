import unittest

from contact import Contact

class TestContact(unittest.TestCase):
    def test_set_name_ok(self):
        contact = Contact()
        contact.name = "Example"
        self.assertEqual("Example", contact.name)

    def test_set_short_name_ok(self):
        contact = Contact()
        contact.name = "E"
        self.assertEqual("E", contact.name)

    def test_set_absent_name_fails(self):
        contact = Contact()
        contact.name = "  "
        self.assertEqual(None, contact.name)