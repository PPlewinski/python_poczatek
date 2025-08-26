from .product_class import print_product

class Order:
    def __init__(self, first_name, last_name, product_list = None):
        self.first_name = first_name
        self.last_name = last_name
        if product_list is None:
            product_list = []
        else:
            self.product_list = product_list

        total_price = 0
        for product in product_list:
            total_price += product.price
        self.total_price = total_price


def print_order(order):
    print(f"Zamówienie na: {order.first_name} {order.last_name}, cena całkowita: {round(order.total_price,2)}")
    print("Lista produktów:")
    for product in order.product_list:
        print_product(product)