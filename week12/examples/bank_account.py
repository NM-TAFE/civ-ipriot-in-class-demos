class BankAccount():
    def __init__(self):
        self._balance = 0

    def current_balance(self):
        return self._balance

    def credit(self, amount, initiator):
        print("Receiving payment from " + initiator)
        if (amount < 0):
            print("Cannot take money during credit!")
            return
        self._balance += amount

    def debit(self, amount, initiator):
        print("Sending payment as " + initiator)
        if (amount < 0):
            print("Cannot add money during debit!")
            return
        self._balance -= amount

bank_account = BankAccount()
bank_account.credit(200, "Example User")
print(bank_account.current_balance())

bank_account.credit(-200, "Example User")
print(bank_account.current_balance())

# You can subvert privacy in Python (easily).
# Technically you can subvert privacy in most languages!
# But we use encapsulation and protect attributes for a reason,
# and there isn't really a good reason to ever do this:

# Again, take a good read through ../lesson.md for more information
# about name mangling in Python.
bank_account._balance = 123500
print(bank_account.current_balance())