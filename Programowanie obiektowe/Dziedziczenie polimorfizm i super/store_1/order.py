import random

from .order_element import OrderElement
from .product import Product
from .tax_calculator import TaxCalculator
from .discount_policy import DiscountPolicy, AbsoluteDiscountPolicy, PercentageDiscountPolicy




class Order:
    MAX_ELEMENTS = 10
    def __init__(self, first_name, last_name, order_elements = None, discount_policy = None):
        self.first_name = first_name
        self.last_name = last_name
        if order_elements is None:
            self._order_elements = []
        else:
            self._order_elements = order_elements
        if len(self._order_elements) > Order.MAX_ELEMENTS:
            self._order_elements = self._order_elements[:Order.MAX_ELEMENTS]
        if discount_policy is None:
            self.discount_policy = DiscountPolicy()
        else:
            self.discount_policy = discount_policy


    @property
    def total_price(self):
        total_price = 0
        for order_element in self._order_elements:
            total_price += order_element.price_calculator()
        return self.discount_policy.apply_discount(total_price)

    def __str__(self):
        buyer_data = f'{self.first_name} {self.last_name}'
        price = f'cena całkowita {self.total_price} PLN'
        list_of_products = "Zamówione produkty\n"
        whole_tax = 0
        for order_element in self._order_elements:
            list_of_products += f'{order_element}\n'
            whole_tax += TaxCalculator.calculate_tax(order_element)
        updated_whole_tax = f'Twój całkowity podatek wynosi {whole_tax}'
        result = "\n".join([buyer_data, price, list_of_products, updated_whole_tax])
        return result

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other):
        if self.first_name != other.first_name or self.last_name != other.last_name:
            return False
        if len(self._order_elements) != len(other.order_elements):
            return False
        for order_element in self._order_elements:
            if order_element not in other.order_elements:
                return False
        return True

    def add_position(self, product, quantity):
        new_element = OrderElement(product, quantity)
        if len(self._order_elements) < Order.MAX_ELEMENTS:
            self._order_elements.append(new_element)

        else:
            print("Osiągnięto limit pozycji")

    @property
    def order_elements(self):
        return self._order_elements

    @order_elements.setter
    def order_elements(self, order_elements):
        if len(order_elements) > Order.MAX_ELEMENTS:
            order_elements = order_elements[:Order.MAX_ELEMENTS]
        self._order_elements = order_elements

class ExpressOrder(Order):
    Delivery_fee = 50

    def __init__(self, first_name, last_name, delivery_date, order_elements = None, discount_policy = None,):
        super().__init__(first_name, last_name, order_elements, discount_policy)
        self.delivery_date = delivery_date

    @property
    def total_price(self):
        return super().total_price + self.Delivery_fee

    def __str__(self):
        return f'{self.first_name} {self.last_name} Opłata za dostawę: {ExpressOrder.Delivery_fee} PLN, Data dostawy: {self.delivery_date}, łączna kwota zamówienia: {self.total_price}'

