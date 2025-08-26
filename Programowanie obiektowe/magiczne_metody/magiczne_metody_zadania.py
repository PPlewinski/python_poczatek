import random


from store.product import Product
from store.order_element import OrderElement
from store.order import Order




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



# def program_runner():
#    order = product_generator()
#    print(order)
if __name__ == '__main__':
    produkt = Product(name = "xd", category = "Kategoria", price = 100)
    produkt_2 = Product(name = "xd", category = "Kategoria", price = 100)
    produkt_3 = Product(name = "xd", category = "Kategoria", price = 100)
    produkt_4 = Product(name = "xd", category = "Kategoria", price = 100)
    result = produkt == produkt_2
    print(result)
    order_element = OrderElement(product = produkt, quantity = 1)
    order_element2 = OrderElement(product = produkt_2, quantity = 1)
    order_element3 = OrderElement(product = produkt_3, quantity = 1)
    order_element4 = OrderElement(product = produkt_4, quantity = 1)
    result_1 = order_element3 == order_element4
    print(result_1)
    order_1 = Order("Paweł",'Plewiński',[order_element, order_element2])
    order_2 = Order("Paweł", "Plewiński", [order_element3, order_element4])
    result_2 = order_1 == order_2
    print(result_2)



#
# class Product:
#     def __init__(self, name, category, price):
#         self.name = name
#         self.category = category
#         self.price = price
#
#     def __str__(self):
#         return f"nazwa {self.name}, kategoria {self.category}, price {self.price}"
#
#
# class OrderElement:
#     def __init__(self, product, quantity):
#         self.product = product
#         self.quantity = quantity
#
#     def price_calculator(self):
#         return self.product.price * self.quantity
#
#     def __str__(self):
#         result = f' {self.quantity} X {self.product.name} = {self.price_calculator()}'
#         return result
#
#
#
# class Order:
#     def __init__(self, first_name, last_name, order_elements=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.order_elements = [] if order_elements is None else order_elements
#         self.total_price = sum(el.price_calculator() for el in self.order_elements)
#
#     def __str__(self):
#        buyer_data = f'Dane kupującego {self.first_name} {self.last_name}'
#        whole_price = f'Cena całkowita {self.total_price}'
#        list_of_products = "Lista produktów:\n"
#        for element in self.order_elements:
#            list_of_products += f"{element}\n"
#        result = "\n".join([buyer_data, whole_price, list_of_products])
#        return result
#
#
#
#
#
#
# def program_runner():
#     # Tego nie ruszaj — po uzupełnieniu __str__ jedynie print(order) ma pokazać ładny opis.
#     p1 = Product("Jabłko", "Owoce", 3.19)
#     p2 = Product("Gruszka", "Owoce", 4.00)
#     e1 = OrderElement(p1, 2)   # 6.38 zł
#     e2 = OrderElement(p2, 2)   # 8.00 zł
#     order = Order("Paweł", "Plewiński", [e1, e2])
#     print(order)  # <— ma użyć Twojego __str__
# if __name__ == '__main__':
#     program_runner()

















