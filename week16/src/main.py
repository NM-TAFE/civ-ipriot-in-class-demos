from payment_methods.credit_card import CreditCard

# This does all the nice logging from the base class, PaymentMethod.
good_pm = CreditCard(1, 2, "4325595359734240", "2/2027", "VISA")
good_pm.pay(500, "AUD")

# So does this, but because it's invalid, it's going to "blow up", or
# in other words, raise an error.
bad_pm = CreditCard(1, 2, None, "2/2027", "VISA")
bad_pm.pay(200, "AUD")