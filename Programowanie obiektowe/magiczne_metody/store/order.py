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

    def __str__(self):
        buyer_data = f'{self.first_name} {self.last_name}'
        price = f'cena całkowita{self.total_price}'
        list_of_products = "Zamówione produkty\n"
        for order_element in self.order_elements:
            list_of_products += f'{order_element}\n'
        result = "\n".join([buyer_data, price, list_of_products])
        return result

    def __len__(self):
        return len(self.order_elements)

    def __eq__(self, other):
        if self.first_name != other.first_name or self.last_name != other.last_name:
            return False
        if len(self.order_elements) != len(other.order_elements):
            return False
        for order_element in self.order_elements:
            if order_element not in other.order_elements:
                return False
        return True