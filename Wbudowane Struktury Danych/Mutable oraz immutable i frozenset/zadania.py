import random


def set_updater(number_set):
    if type(number_set) == set:
        some_number = random.randint(1, 10)
        return number_set.add(some_number)
    elif type(number_set) == frozenset:
        some_number = {random.randint(1, 10)}
        return number_set.union(some_number)
    else:
        return print("podaj set jako argument do funkcji")
some_set = {}
some_frozen_set = frozenset({})
while len(some_frozen_set) < 10:
    some_frozen_set = set_updater(some_frozen_set)
    print(some_frozen_set)
    print("Dobraliśmy liczby")
    continue
print('wszytsko gitez')