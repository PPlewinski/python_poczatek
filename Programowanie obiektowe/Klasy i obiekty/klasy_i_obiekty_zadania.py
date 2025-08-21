
class Product:
    pass

class Order:
    pass

class Apple:
    pass

class Potato:
    pass

if __name__ == '__main__':
    apple = Apple()
    potato = Potato()
    product = Product()
    order = Order()
    print(type(apple))
    print(type(potato))
    print(type(product))
    print(type(order))

    order = [Order(), Order(), Order(), Order(), Order()]
    print(order)

    product = {
        "jabłka": Product(),
        "ziemniaki": Product(),
        "fasola": Product(),
        "kalafiory": Product(),
        "pomidory": Product(),
    }
    print(product)