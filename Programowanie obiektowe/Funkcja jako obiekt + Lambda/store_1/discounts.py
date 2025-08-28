class Discounts:

    @staticmethod
    def default_policy(total_price):
        return total_price
    @staticmethod
    def regular_clients_policy(total_price):
        return total_price * 0.95
    @staticmethod
    def holiday_discount(total_price):
        if total_price > 100:
            return total_price - 20
        return total_price
