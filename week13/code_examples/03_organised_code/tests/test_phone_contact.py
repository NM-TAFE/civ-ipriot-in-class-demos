import unittest

from phone_contact import PhoneContact

class TestPhoneContact(unittest.TestCase):
    def test_full_phone_number(self):
        phone = PhoneContact()
        phone.phone_number = "412345678"
        phone.area_code = "61"
        self.assertEqual(phone.full_phone_number, "61-412345678")

    def test_set_phone_number_fails_for_absent_values(self):
        phone = PhoneContact()
        phone.phone_number = ""
        self.assertEqual(phone.phone_number, None)

    def test_set_phone_number_fails_for_alpha_charas(self):
        phone = PhoneContact()
        phone.phone_number = "abc"
        self.assertEqual(phone.phone_number, None)
        # self.assertFalse(phone.valid())

    def test_set_phone_number_succeeds_for_numeric_charas(self):
        phone = PhoneContact()
        phone.phone_number = "413456789"
        self.assertEqual(phone.phone_number, "413456789")

    def test_set_area_code_fails_for_absent_values(self):
        phone = PhoneContact()
        phone.area_code = ""
        self.assertEqual(phone.area_code, None)

    def test_set_area_code_fails_for_alpha_charas(self):
        phone = PhoneContact()
        phone.area_code = "abc"
        self.assertEqual(phone.area_code, None)

    def test_set_area_code_succeeds_for_numeric_charas(self):
        phone = PhoneContact()
        phone.area_code = "61"
        self.assertEqual(phone.area_code, "61")
