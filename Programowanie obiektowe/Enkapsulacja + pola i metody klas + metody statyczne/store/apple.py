class Apple:
    def __init__(self, brand, price, size):
        self.brand = brand
        self.price = price
        self.size = size
    def price_calculator(self, quantity):
        return quantity * self.price
    def __repr__(self):
        return f"<Apple brand='{self.brand}', size='{self.size}', price='{self.price}'>"