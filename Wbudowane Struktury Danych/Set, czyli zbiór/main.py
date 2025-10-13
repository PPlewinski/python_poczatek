import random

flavours = ["Malinowy", "Truskawkowy",  'Jagodowy']
alice_favourite_flavours = {"Pistacjowy", "Truskawkowy", "Orzechowy"}
bob_favourite_flavours = set(flavours)

# empty_set = set()
# print(empty_set)

# print(bob_favourite_flavours)

# bob_favourite_flavours.add('borówkowy')
# print(bob_favourite_flavours)

# bob_favourite_flavours.remove('Malinowy')
# print(bob_favourite_flavours)

# bob_favourite_flavours.discard('Jagodowy')
# print(bob_favourite_flavours)

# print(bob_favourite_flavours.pop())

# copy_of_flavourst = bob_favourite_flavours.copy()
# bob_favourite_flavours.clear()
# print(copy_of_flavourst)
# print(bob_favourite_flavours)
# alice_favourite_flavours.update(bob_favourite_flavours)
# print(alice_favourite_flavours)

# print(len(bob_favourite_flavours))

# set_of_set = {{"Słony karmel", "Mango"}, {"Truskawkowy", "Śmietankowy"}}
# print(set_of_set)
print(bob_favourite_flavours)
print(alice_favourite_flavours)

all_flavours = bob_favourite_flavours.union(alice_favourite_flavours)
print(all_flavours)

# common_flavours = bob_favourite_flavours.intersection(alice_favourite_flavours)
# print(common_flavours)

# different_flavours = bob_favourite_flavours.difference(alice_favourite_flavours)
# print(different_flavours)

print(bob_favourite_flavours.issubset(all_flavours))

numbers = [random.randint(0, 40) for _ in range(100)]
no_duplicates = set(numbers)
print(len(numbers))
print(len(no_duplicates))

digits = set([number for number in range(10)])
print(f"Czy udało się wylosować wszystkie cyfry? {digits.issubset(no_duplicates)}")

