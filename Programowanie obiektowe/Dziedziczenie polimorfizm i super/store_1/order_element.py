from dataclasses import dataclass
from .tax_calculator import TaxCalculator
from .product import Product

@dataclass
class OrderElement:
    product: Product
    quantity: int

    def price_calculator(self):
        return self.product.price * self.quantity

    def __str__(self):
        result = f' {self.product.__str__()}\n ilosc {self.quantity} podatek {TaxCalculator.calculate_tax(self)}'
        return result



