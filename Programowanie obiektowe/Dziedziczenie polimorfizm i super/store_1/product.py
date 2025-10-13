import random
from dataclasses import dataclass
from enum import Enum

class ProductCategory(Enum):
    FOOD = 'Jedzenie'
    DAIRY = 'Nabiał'
    DRINKS = 'Napoje'
    FURNITURE = 'Meble'
@dataclass
class Product:
    name:str
    category:ProductCategory
    price:float
    identifier: int

    def __str__(self):
        return f'nazwa:{self.name} kategoria:{self.category.value} cena:{self.price}'

