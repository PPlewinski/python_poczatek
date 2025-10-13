from .product import Product
from dataclasses import dataclass


class ProductExpiry(Product):
    year_of_prod: int
    ex_year: int

    def does_expired(self, current_year):
        if self.year_of_prod + self.ex_year >= current_year:
            return 'Produkt jest jeszcze ważny'
        else:
            return 'Produkt jest już przeterminowany'