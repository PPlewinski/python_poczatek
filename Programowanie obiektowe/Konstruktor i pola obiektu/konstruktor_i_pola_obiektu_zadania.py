import random
class Product:
    def __init__(self, name, category, price):
        self.price = price
        self.category = category
        self.name = name

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

class Apple:
    def __init__(self, brand, price, size):
        self.brand = brand
        self.price = price
        self.size = size


class Potato:
    def __init__(self, brand, size, price):
        self.brand = brand
        self.size = size
        self.price = price

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

def print_order(order):
    print(f"Zamówienie na: {order.first_name} {order.last_name}, cena całkowita: {round(order.total_price,2)}")
    print("Lista produktów:")
    for product in order.product_list:
        print_product(product)

def program_runner():
    product_1 = Product("Jabłko", "Owoce", 3.19)
    product_2 = Product("Gruszka", "Owoce", 4.20 )
    print_product(product_1)
    print_product(product_2)
    order_1 = Order("Paweł", "Plewiński", product_list= product_generator())
    print_order(order_1)
if __name__ == '__main__':
    program_runner()



# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#
#
# class Library:
#     def __init__(self, name, book_list = None):
#         self.name = name
#         if book_list is None:
#             book_list = []
#         self.book_list = book_list
#         total_number_of_books = 0
#         for book in book_list:
#             total_number_of_books += 1
#         self.total_number_of_books = total_number_of_books
#
# class Reader:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
# def info_receiver(name, surname):
#     name_info = input(name)
#     surname_info = input(surname)
#     return name_info, surname_info
#
#
# def project_run():
#     book_1 = Book(title="Kubuś Puchatek", author="Niewiem", price=100)
#     print(book_1.title, book_1.author, book_1.price)
#     library_1 = Library(name="Bibioteka 1", book_list = [book_1])
#     print(library_1.name, library_1.book_list, library_1.total_number_of_books)
#     name_1, surname_1 = info_receiver("Jak masz na imię", "Jak masz na nazwisko")
#     reader_1 = Reader(name = name_1, surname = surname_1)
#     print(reader_1.name, reader_1.surname)
#     print(book_1)
#
#
# if __name__ == '__main__':
#     project_run()




#
# class Car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
# class Garage:
#     def __init__(self, owner, vehicle_list = None):
#         self.owner = owner
#         if vehicle_list is None:
#             self.vehicle_list = []
#         else:
#             self.vehicle_list = vehicle_list
#
#         total_vehicle_count = len(self.vehicle_list)
#         self.total_vehicle_count = total_vehicle_count
#
# class Bike:
#     def __init__(self, brand, size, price):
#         self.brand = brand
#         self.size = size
#         self.price = price
#
# class Scooter:
#     def __init__(self, brand, size, price):
#         self.brand = brand
#         self.size = size
#         self.price = price
#
# def program_runner():
#     car_1 = Car('BMW', 'M3', 100)
#     car_2 = Car('BMW', 'M4', 200)
#     print(car_1.brand, car_1.model, car_1.price)
#     print(car_2.brand, car_2.model, car_2.price)
#     garage_1 = Garage( owner='Paweł', vehicle_list=[car_1, car_2])
#     print(garage_1.owner, garage_1.vehicle_list, garage_1.total_vehicle_count)
#     bike_1 = Bike( brand='BMW', size=10, price=100)
#     print(bike_1.brand, bike_1.size, bike_1.price)
#     scooter_1 = Scooter(brand='BMW', size=10, price=13232)
#     print(scooter_1.brand, scooter_1.size, scooter_1.price)
#
#
# if __name__ == '__main__':
#     program_runner()



































