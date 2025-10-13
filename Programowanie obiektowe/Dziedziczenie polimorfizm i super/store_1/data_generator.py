import random
from .product import Product, ProductCategory
from .order_element import OrderElement
from .order import  Order


MIN_ELEMENTS_QUAN = 1
MAX_ELEMENTS_QUAN= 10
MIN_PRICE = 20
MAX_PRICE = 300

def order_generator(number_of_products=None):
    if number_of_products is None:
        number_of_products = random.randint(1, Order.MAX_ELEMENTS)
    order_elements = []
    for product in range(number_of_products):
        name = f"Produkt nr. {product}"
        category = ProductCategory.FOOD
        random_price = random.randint(MIN_PRICE, MAX_PRICE)
        price = random_price
        identifier = random.randint(1, 1000)
        product = Product(name, category, price, identifier)
        quan = random.randint(MIN_ELEMENTS_QUAN, MAX_ELEMENTS_QUAN)
        order_elements.append(OrderElement(product, quan))

    order = Order("Paweł", "Plewiński", order_elements)
    return order
