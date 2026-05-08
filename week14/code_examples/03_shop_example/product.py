class Product:
    def __init__(self):
        self.name = ""
        self.category = ""
        self.quantity = 0
        self.unit_price_cents = 0

    def sell(self):
        if self.quantity < 1:
            print(f"{self.name}: You can't sell what you don't have")
            return
        self.quantity -= 1
        return self.unit_price_cents