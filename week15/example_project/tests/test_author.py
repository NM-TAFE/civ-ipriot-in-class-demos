from author import Author
from unittest import TestCase

class TestAuthor(TestCase):
    def test_blank_name_rejected(self):
        original_name = "Martha Wells"
        test_author = Author(original_name)
        self.assertEqual(test_author.name, original_name)
        test_author.name = ""
        self.assertEqual(test_author.name, original_name)

    def test_filled_name_accepted(self):
        original_name = "David Barnes"
        test_author = Author(original_name)
        self.assertEqual(test_author.name, original_name)
        test_author.name = "Michael Kolling"
        self.assertEqual(test_author.name, "Michael Kolling")

    # The next three tests demonstrate assertTrue and assertFalse
    # However, they exhibit poor encapsulation, as is_valid
    # should truthfully either be private and untested,
    # or the public member of another class.
    def test_is_valid_disallows_empty(self):
        author = Author(None)
        self.assertFalse(author.is_valid(""))

    def test_is_valid_disallows_none(self):
        author = Author(None)
        self.assertFalse(author.is_valid(None))

    def test_is_valid_allows_string(self):
        author = Author(None)
        self.assertTrue(author.is_valid("A"))

