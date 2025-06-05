from payment_methods.payment_method import PaymentMethod
import random

class CreditCard(PaymentMethod):
    def __init__(self, billing_details_id, customer_id, cc_number, expiry_date, type):
        super().__init__(billing_details_id, customer_id)
        self.cc_number = cc_number
        self.expiry_date = expiry_date
        self.type = type

    def is_valid(self):
        if (not super().is_valid()):
            return False

        return (self.cc_number and self.expiry_date and self.type)

    # Obviously very unrealistic -- this would in reality be several
    # calls to various CC APIs, covering such things as "getting credit card info";
    # "authorising funds" etc
    # This also violates "telling" rather than "asking".
    # Here, the class CreditCard is "at the mercy" of its "type"
    # In reality, it might have been nicer to have a subclass per provider, doing
    # provider-specific things.
    # eg: credit_card.Amex(), or credit_card.Visa(), which have their own implementations.
    def _get_cc_endpoint(self):
       if self.type == "VISA":
           return "https://visa.com"
       elif self.type == "MASTERCARD":
           return "https://mastercard.com"
       elif self.type == "AMEX":
           return "https://amex.com"

    # Your own payment_implementation should return a bool
    def _payment_implementation(self, amount, currency):
        endpoint = self._get_cc_endpoint()

        print(f"{endpoint}?cc_number={self.cc_number}&expiry={self.expiry_date}&amount={amount}&currency={currency}")
        response = random.choice([True, False]) # fake API call

        return response