class OrderElement:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def price_calculator(self):
        return self.product.price * self.quantity

    def __str__(self):
        result = f' {self.product.__str__()}\n ilosc {self.quantity}'
        return result

    def __eq__(self, other):
        return self.product == other.product and self.quantity == other.quantity