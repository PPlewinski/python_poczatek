import random
class Product:
    def __init__(self, name, category, price):
        self.price = price
        self.category = category
        self.name = name

def product_generator():
    number_of_products = random.randint(1, 20)
    list_of_products = []
    for product in range(number_of_products):
        name = f"Produkt nr. {product}"
        category = f"Kategoria nr. {product}"
        random_price = random.randint(1, 100)
        price =  random_price
        list_of_products.append(Product(name, category, price))
    return list_of_products

def print_product(product):
    print(f"Produkt: {product.name}, Kategoria: {product.category}, Cena: {product.price}")
