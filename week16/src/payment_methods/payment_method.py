from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, billing_details_id, customer_id):
        self.billing_details_id = billing_details_id
        self.customer_id = customer_id

    def pay(self, amount, currency):
        if(not self.is_valid()):
            print("PaymentMethod is not valid")
            raise TypeError("Object does not have a customer or billing details")
        print(f"Customer {self.customer_id} attempted a payment of {amount} in {currency}")
        result = self._payment_implementation(amount, currency)
        if result:
            print(f"Customer {self.customer_id} successfully made a payment of {amount} in {currency}")
        else:
            print(f"Customer {self.customer_id} failed to make a payment of {amount} in {currency}")

        return result

    def is_valid(self):
        if (self.billing_details_id == None or self.customer_id == None):
            return False

        return True

    @abstractmethod
    def _payment_implementation(self, amount, currency):
        pass

