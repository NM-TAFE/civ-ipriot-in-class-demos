import unittest

from email_contact import EmailContact

class TestEmailContact(unittest.TestCase):
    def test_set_valid_email_succeeds(self):
        email_contact = EmailContact()
        email_contact.email = "test@example.com"
        self.assertEqual("test@example.com", email_contact.email)

    def test_set_invalid_email_fails(self):
        email_contact = EmailContact()
        email_contact.email = "example"
        self.assertNotEqual("example", email_contact.email)