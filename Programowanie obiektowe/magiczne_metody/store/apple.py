from dataclasses import dataclass
@dataclass
class Apple:
    brand: str
    size: str
    price: float
    def price_calculator(self, quantity):
        return quantity * self.price
    def __repr__(self):
        return f"<Apple brand='{self.brand}', size='{self.size}', price='{self.price}'>"