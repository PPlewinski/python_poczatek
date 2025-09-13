


from store_1.product import Product
from store_1.order_element import OrderElement
from store_1.order import Order
from store_1.discounts import Discounts
from store_1.data_generator import order_generator
from store_1.order import Order







def program_runner():
    order = order_generator()
    for order_ment in order.order_elements:
        print(order_ment)
    print(order.total_price)

    order.order_elements = [order_element, order_element2, order_element3, order_element4]
    for order_ment in order.order_elements:
        print(order_ment)
    print(order.total_price)



if __name__ == '__main__':
    produkt = Product(name = "xd", category = "Kategoria", price = 100)
    produkt_2 = Product(name = "xd", category = "Kategoria", price = 210)
    produkt_3 = Product(name = "xd", category = "Jedzenie", price = 102)
    produkt_4 = Product(name = "xd", category = "Owoce i Warzywa", price = 100)
    # result = produkt == produkt_2
    # print(result)
    order_element = OrderElement(product = produkt_2, quantity = 1)
    order_element2 = OrderElement(product = produkt_3, quantity = 1)
    order_element3 = OrderElement(product = produkt_4, quantity = 1)
    order_element4 = OrderElement(product = produkt_4, quantity = 1)
    # result_1 = order_element3 == order_element4
    # print(result_1)
    # order_1 = Order("Paweł",'Plewiński',[order_element, order_element2])
    # order_2 = Order("Paweł", "Plewiński", [order_element3, order_element4])
    # result_2 = order_1 == order_2
    # print(result_2)

    program_runner()



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