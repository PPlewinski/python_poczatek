


from store.product import Product
from store.order_element import OrderElement
from store.order import Order








def program_runner():
   order = Order(first_name="Paweł", last_name="Plewiński", order_elements=[order_element, order_element2, order_element3])
   print(order)




if __name__ == '__main__':
    # produkt = Product(name = "xd", category = "Kategoria", price = 100)
    produkt_2 = Product(name = "xd", category = "Kategoria", price = 100)
    produkt_3 = Product(name = "xd", category = "Jedzenie", price = 100)
    produkt_4 = Product(name = "xd", category = "Owoce i Warzywa", price = 100)
    # result = produkt == produkt_2
    # print(result)
    order_element = OrderElement(product = produkt_2, quantity = 1)
    order_element2 = OrderElement(product = produkt_3, quantity = 1)
    order_element3 = OrderElement(product = produkt_4, quantity = 1)
    # order_element4 = OrderElement(product = produkt_4, quantity = 1)
    # result_1 = order_element3 == order_element4
    # print(result_1)
    # order_1 = Order("Paweł",'Plewiński',[order_element, order_element2])
    # order_2 = Order("Paweł", "Plewiński", [order_element3, order_element4])
    # result_2 = order_1 == order_2
    # print(result_2)
    program_runner()









































