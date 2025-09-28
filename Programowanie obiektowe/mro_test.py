
class Grandparent:
    def say_hello(self):
        print('Dziadek')

class Parentone(Grandparent):
    # pass
    def say_hello(self):
        print('Tata')

class Parentwo(Parentone, Grandparent):
    # pass
    def say_hello(self):
        print('Mama')

class Child(Parentwo, Parentone, Grandparent):
    pass

dziecko = Child()
dziecko.say_hello()