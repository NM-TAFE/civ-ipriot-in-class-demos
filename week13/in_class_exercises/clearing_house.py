class CreditCard:
    ...
class PayPal:
    def process_payment(self, amount):
        print("PayPal processing")

class ClearingHouse:
    def process_transactions(self, amount, processor):
        processor.process_payment(amount)

transactions = {"PayPal": [100, 200, 350],
                "CC": [50, 30, 20]}

ch = ClearingHouse()
for transaction in transactions["PayPal"]:
    ch.process_transactions(transaction, PayPal())

for transaction in transactions["CC"]:
    ch.process_transactions(transaction, CreditCard())
