import random

expenditures = {
        "prąd": [250],
        "woda": [30.45],
        "zakupy": [
            120.15,
            170.53,
            20.15
        ]
    }
# print(expenditures)
# expenditures.clear()
# print(expenditures)
# copy = expenditures.copy()
# print(copy)

# water = expenditures.get("woda")
# print(water)

# cookies = expenditures.get("Ciasteczka", [8282])
# print(cookies)
#
# expenditures.update(Ciasteczka = [323])
# print(expenditures)
# expenditures.update(woda = [323])
# print(expenditures)

expenditures_names = ['Woda', 'Prąd', 'Gaz']
ezpenditures = {expenditure_name: random.randint(1,100) for expenditure_name in expenditures_names}
print(ezpenditures)