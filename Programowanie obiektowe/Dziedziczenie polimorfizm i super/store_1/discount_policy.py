

class DiscountPolicy:
    def apply_discount(self,total_price):
        return total_price

class PercentageDiscountPolicy(DiscountPolicy):
    def __init__(self, discount_factor):
        self.discount_factor = discount_factor

    def apply_discount(self,total_price):
        return total_price * (1 - self.discount_factor)

class AbsoluteDiscountPolicy(DiscountPolicy):
    def __init__(self, discount_factor):
        self.discount_factor = discount_factor

    def apply_discount(self,total_price):
        return total_price - self.discount_factor
