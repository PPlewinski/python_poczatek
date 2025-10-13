import random
def product_delivery():
    products = [
        'Masło',
        "Jajka",
        "Chleb",
        "Pierogi",
        "Mleko",
        "Mąka",
        "Szynka",
        "Ser",
        "Śmietana",
        "Twaróg"
    ]
    return [products[random.randint(0, len(products) - 1)] for _ in range(5)]