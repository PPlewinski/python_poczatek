class Potato:
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price
    def price_calculator(self, quantity):
        return quantity * self.price
    def __repr__(self):
        return f"<Potato brand='{self.brand}', size='{self.size}', price='{self.price}'>"