import random
class Product:
    def __init__(self, name, category, price):
        self.price = price
        self.category = category
        self.name = name

    def print_product(self):
        print(f"nazwa {self.name}, kategoria {self.category}, cena {self.price}")

class Order:
    def __init__(self, first_name, last_name, order_elements = None):
        self.first_name = first_name
        self.last_name = last_name
        if order_elements is None:
            self.order_elements = []
        else:
            self.order_elements = order_elements

        total_price = 0
        for order_element in self.order_elements:
            total_price += order_element.price_calculator()
        self.total_price = total_price

    def print_order(self):
        print(f"Zamówienie: {self.first_name}, {self.last_name}, o łącznej cenie:{self.total_price}")
        print("Lista produktów")
        for element in self.order_elements:
           element.print_self()


class OrderElement:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def price_calculator(self):
        return self.product.price * self.quantity

    def print_self(self):
        self.product.print_product()
        print(self.quantity)




class Apple:
    def __init__(self, brand, price, size):
        self.brand = brand
        self.price = price
        self.size = size
    def price_calculator(self, quantity):
        return quantity * self.price


class Potato:
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price
    def price_calculator(self, quantity):
        return quantity * self.price



def product_generator():
    number_of_products = random.randint(1, 20)
    order_elements = []
    for product in range(number_of_products):
        name = f"Produkt nr. {product}"
        category = f"Kategoria nr. {product}"
        random_price = random.randint(1, 100)
        price =  random_price
        product = Product(name, category, price)
        quan = random.randint(1, 20)
        order_elements.append(OrderElement(product, quan))

    order = Order("Paweł", "Plewiński", order_elements)
    return order



def program_runner():
   order = product_generator()
   order.print_order()
if __name__ == '__main__':
    program_runner()















# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#
#     def print_info(self):
#         print(f"Informacje o samochodzie {self.brand} {self.model} {self.year}")
#
#
# class Garage:
#     def __init__(self, owner, car_list = None):
#         self.owner = owner
#         if car_list is None:
#             self.car_list = []
#         else:
#             self.car_list = car_list
#
#     def add_car(self, car):
#         self.car_list.append(car)
#
#     def show_info(self):
#         for car in self.car_list:
#             car.print_info()
#
#
# def program_runner():
#     car_1 = Car(brand = "Toyota", model = "Corrolla", year = 2020)
#     car_2 = Car(brand = "Toyota", model = "Prius", year = 2015)
#     car_1.print_info()
#     car_2.print_info()
#     garage_1 = Garage(owner = "Paweł", car_list = [car_1, car_2])
#     garage_1.show_info()
#
# if __name__ == '__main__':
#     program_runner()

















