from .product import Product

class ProductExpiry(Product):
    def __init__(self, name, category, price, year_of_prod, ex_year):
        super().__init__(name, category, price)
        self.ex_year = ex_year
        self.year_of_prod = year_of_prod

    def does_expired(self, current_year):
        if self.year_of_prod + self.ex_year >= current_year:
            return 'Produkt jest jeszcze ważny'
        else:
            return 'Produkt jest już przeterminowany'