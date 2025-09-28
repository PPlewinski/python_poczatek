class TaxCalculator:
    @staticmethod
    def calculate_tax(order_element):
        if order_element.product.category == 'Owoce i Warzywa':
            return order_element.price_calculator() * 0.05
        elif order_element.product.category == 'Jedzenie':
            return order_element.price_calculator() * 0.08
        else:
            return order_element.price_calculator() * 0.20



