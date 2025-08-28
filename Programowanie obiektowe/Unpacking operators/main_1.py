import random
#
# def text_generator(*args):
#     result = ''
#     for arg in args:
#         result += str(arg)
#         result += '-'
#     return result[:-1]
# runner = text_generator("Siema", "eniu", "jestem", "Paweł")
# print(runner)

def taker(**kwargs):
    for first, second in kwargs.items():
        print(f'{first} = {second}')

values = {
    "first name": "Paweł",
    "Last name": "Plewiński",
    "age": 18
}

values_1 = {
    "email": "rrrrrrrr",
    "phone number": "726 432 531",
}
joined_values = {**values, **values_1}
taker(**values, **values_1)
taker(**joined_values)

# list_1 = []
# random_numbers = random.randint(1, 100)
# for _ in range(random_numbers):
#     list_1.append(random.randint(1, 100))
#
# list_2 = []
# random_numbers = random.randint(1, 100)
# for _ in range(random_numbers):
#     list_2.append(random.randint(1, 100))
# print(list_1)
# print(list_2)
# joined_list = [*list_1, *list_2]
# print(joined_list)