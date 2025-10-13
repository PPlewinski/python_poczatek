# shopping_list = ["woda", "chleb", "mąka"]
# my_list = shopping_list
# your_list = shopping_list
#
# print("shopping_list:", shopping_list)
# print("my_list:", my_list)
# print("your_list:", your_list)
#
# print(id(shopping_list), id(my_list), id(your_list))
#
# print()
# print("Dodaję ciastka do swojej listy...")
# my_list.append("ciastka")
#
# print("shopping_list:", shopping_list)
# print("my_list:", my_list)
# print("your_list:", your_list)
#
# print(id(shopping_list))
# print(id(my_list))
# print(id(your_list))
#
# hello_str = "Hello"
# my_str = hello_str
# your_str = hello_str
#
# print("hello_str:", hello_str)
# print("my_str:", my_str)
# print("your_str:", your_str)
#
# print(id(hello_str))
# print(id(my_str))
# print(id(your_str))
#
# print()
# print("Zmieniam swoje przywitanie...")
# my_str += " World!"
#
# print("hello_str:", hello_str)
# print("my_str:", my_str)
# print("your_str:", your_str)
#
# print(id(hello_str))
# print(id(my_str))
# print(id(your_str))

flavours = ["Malinowy", "Truskawkowy", "Jagodowy"]
bob_favourite_flavours = frozenset(flavours)
print(type(bob_favourite_flavours))
alice_favourite_flavours = frozenset({"Pistacjowy", "Truskawkowy", "Orzechowy"})
print(alice_favourite_flavours)

alice_favourite_flavours = frozenset(["Pistacjowy", "Truskawkowy", "Orzechowy", "Orzechowy", "Orzechowy"])
print(alice_favourite_flavours)
common_flavours = bob_favourite_flavours.intersection(alice_favourite_flavours)
print(common_flavours)
all_flavours = bob_favourite_flavours.union(alice_favourite_flavours)
print(all_flavours)