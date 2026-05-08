class Department:
    def __init__(self, name=""):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Department: {self.name}, with {len(self.products)} products"