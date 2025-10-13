



from store_1.order_element import OrderElement
from store_1.order import Order
from store_1.discounts import Discounts
from store_1.data_generator import order_generator
from store_1.order import Order
from store_1.porduct_expir import ProductExpiry
from store_1.order import ExpressOrder
from store_1.product import Product, ProductCategory
from store_1.discount_policy import DiscountPolicy, AbsoluteDiscountPolicy, PercentageDiscountPolicy
from store_1.delivery import product_delivery






# def program_runner():
    # order = order_generator()
    # for order_ment in order.order_elements:
    #     print(order_ment)
    # print(order.total_price)
    #
    # order.order_elements = [order_element, order_element2, order_element3, order_element4]
    # for order_ment in order.order_elements:
    #     print(order_ment)
    # print(order.total_price)
    # produkt = ProductExpiry(name='Masło', price=100, category = 'Nabiał', year_of_prod=2020, ex_year=6)
    # print(produkt)
    # print(produkt.does_expired(2030))
    # order_del = ExpressOrder(first_name='dads', last_name='dadq', order_elements=[order_element, order_element2, order_element3, order_element4],
    #                          delivery_date='12/10/2025', )
    # print(order_del)

    # order = Order(first_name='fijwifi', last_name='dasd',
    #               order_elements = [order_element, order_element2, order_element3, order_element4])
    # print(order)
    # print(order.order_elements)
    # order = order_generator()
    # print(order.order_elements)
    # new_dict = {identifier +1: product
    #             for identifier,product in order.order_elements.items()}
    # print(new_dict)
    # order.order_elements.update(new_dict)
    # print(order.order_elements)

    # products = {
    #     'Masło',
    #     "Jajka",
    #     "Chleb",
    #     "Pierogi",
    #     "Mleko",
    #     "Mąka",
    #     "Szynka",
    #     "Ser",
    #     "Śmietana",
    #     "Twaróg"
    # }
    #
    # delivery = []
    # while True:
    #     if not set(delivery) == set(products):
    #         new_products = product_delivery()
    #         delivery += new_products
    #         print(f'otrzymano produktu {new_products}')
    #         missing_products = products.difference(delivery)
    #         print(f'brakuje {missing_products}')
    #         continue
    #     print('Dostawa wykonana')
    #     break






if __name__ == '__main__':
    # produkt = Product(name = "xd", category = "Kategoria", price = 100)
    # produkt_2 = Product(name = "xd", category = "Kategoria", price = 210)
    # produkt_3 = Product(name = "xd", category = "Jedzenie", price = 102)
    # produkt_4 = Product(name = "xd", category = "Owoce i Warzywa", price = 100)
    # result = produkt == produkt_2
    # print(result)
    # order_element = OrderElement(product = produkt_2, quantity = 1)
    # order_element2 = OrderElement(product = produkt_3, quantity = 1)
    # order_element3 = OrderElement(product = produkt_4, quantity = 1)
    # order_element4 = OrderElement(product = produkt_4, quantity = 1)
    # result_1 = order_element3 == order_element4
    # print(result_1)
    # order_1 = Order("Paweł",'Plewiński',[order_element, order_element2])
    # order_2 = Order("Paweł", "Plewiński", [order_element3, order_element4])
    # result_2 = order_1 == order_2
    # print(result_2)
    #
    # program_runner()
    # def equality_check():
    #     parameters_test = [
    #         ('Jajka', 'produkt odzwierzęcy', 12, 'Jajka', 'produkt odzwierzęcy', 12, True),
    #         ('Mleko', ' nabiał', 4, 'Śmietana', ' nabiał', 5, False),
    #         ('Wołowina', 'mięso', 20, 'Wieprzowina', 'mięso', 18, False),
    #     ]
    #     for params in parameters_test:
    #         name, category, price, other_name, other_category, other_price, true_value = params
    #         product = Product(name, category, price)
    #         other_product = Product(other_name, other_category, other_price)
    #         result = product == other_product
    #         if result == true_value:
    #             print('Wszystko OK')
    #         else:
    #             print(f'Problem z parametrami {product} {other_product}')
    #
    # equality_check()
    # kategoria_jedzenie = ProductCategory.FOOD
    # print(kategoria_jedzenie.value)
    # product = Product(name = 'Czipsy', price = 5.99, identifier= 2222, category= kategoria_jedzenie)
    # print(product)
    order = order_generator()
    for order_element in order.order_elements:
        print(order_element)














# class Osoba:
#     def __init__(self, imie):
#         self._imie = imie
#
#     @property
#     def imie(self):
#         return self._imie
#     @imie.setter
#     def imie(self, imie):
#         if imie == "":
#             raise ValueError("Imię nie może być puste")
#         self._imie = imie
#
# osoba = Osoba("dsd")
# print(osoba.imie)
# osoba.imie = ""
# print(osoba.imie)

# class Temperature:
#     def __init__(self, temperature):
#         self._temperature = temperature
#
#     @property
#     def temperature(self):
#         return self._temperature
#
#     @temperature.setter
#     def temperature(self, value):
#         if value < -273.15:
#             raise ValueError("Temperature must be greater than or equal to -273.15 C")
#         self._temperature = value
#
#
# T = Temperature(123)
# print(T.temperature)
# print(T.temperature)
# T.temperature = -300
# print(T.temperature)

# class Email:
#     def __init__(self, email):
#         self._email = email
#
#     @property
#     def email(self):
#         return self._email
#
#     @email.setter
#     def email(self, email):
#         if '@' not in email:
#             raise ValueError('Email address must contain "@"')
#         self._email = email
#
# E = Email("@fsfa")
# print(E.email)
# E.email = "dsdcf"
# print(E.email)

# class Animal:
#     def speak(self):
#         print("Dżwięk")
#
# class Cat(Animal):
#     def speak(self):
#         print("Miau")
#
# kot =

# class Vehicle:
#     def move(self):
#         print("Moving on")
#
# class Car(Vehicle):
#     def honk(self):
#         print("Beep beep")
#
# car = Car()
# car.move()
# car.honk()



# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         return f"Name: {self.name}"
#
# class Employee(Person):
#     def __init__(self, name, psoition):
#         super().__init__(name)
#         self.psoition = psoition
#
#     def info(self):
#         return f'{self.name} Stanowisko: {self.psoition}'
#
#
# pracownik = Employee("Michał", "Junior marketing assistant")
# print(pracownik.info())