import random


def name_reder():
    imie = input("Podaj imie: ").strip()
    nazwisko = input("Podaj nazwisko: ").strip()
    print("Nazywasz się %s %s" % (imie,nazwisko))

name_reder()


# def random_id_generator():
#     identifier = str(random.randint(1,99999)).zfill(5)
#     print(identifier)
#
# random_id_generator()






# def color_reader():
#     kolory = input("Podaj swoje ulubione kolory").lower()
#     if kolory.find('niebieski') > -1:
#         return 'Masz tam niebieski'
#     else:
#         return 'Nie ma tam niebieskiego'
#
# print(color_reader())
