from Store import order_class
from Store import product_class


def program_runner():
    product_1 = product_class.Product("Jabłko", "Owoce", 3.19)
    product_2 = product_class.Product("Gruszka", "Owoce", 4.20 )
    product_class.print_product(product_1)
    product_class.print_product(product_2)
    order_1 = order_class.Order("Paweł", "Plewiński", product_list= product_class.product_generator())
    order_class.print_order(order_1)
if __name__ == '__main__':
    program_runner()