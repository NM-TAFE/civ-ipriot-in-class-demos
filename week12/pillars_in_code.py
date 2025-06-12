class BankAccount:

    def __init__(self, name, account_number) -> None:
        self._name = name
        self._account_number = account_number
        self._balance = 0

    # abstraction
    def withdraw(self, value):
        if value <= 0:
            raise ValueError("Amount must positive")
        if value > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= value


    def deposit(self, value):
        if value <= 0:
            raise ValueError("Amount must positive")
        self._balance += value

    # encapsulation
    def update_balance(self, value):
        if self._balance + value < 0:
            raise ValueError("Insufficient Funds")
        self._balance += value
# access modifiers: protected/private

raf = BankAccount("Raf's account", "12345")
amanda = BankAccount("Amanda's account", "12346")

raf.update_balance(-1000)
raf._balance += 1000 # YOU'RE FIRED

amanda.balance += 100
amanda.balance += 42
raf.balance -= 42
if raf.balance - 1300 < 0:
    print("No money")
else:
    raf.balance -= 1300
raf.balance = "$$$$" # oi, just use numbers!

print("Raf's balance:", raf.balance)
print("Amanda's:", amanda.balance)
