class Product:
    def __init__(self, name, category, price):
        self.price = price
        self.category = category
        self.name = name

    def __str__(self):
        return f'nazwa:{self.name} kategoria:{self.category} cena:{self.price}'

    def __eq__(self, other):
        return self.name == other.name and self.category == other.category and self.price == other.price