# Zadanie 1



first_list = [number for number in range(1,31) if number % 3 == 0]
second_list = [number for number in range(1,31) if number % 5 == 0]

final_list = first_list + second_list
print(final_list)


# Zadanie 2



def list_printer():
    fav_sports = input("podaj listę ulubionych sportów, rozdzielając je przecinkiem")
    fav_sports = fav_sports.split(",")
    for index,item in enumerate(fav_sports):
        if index % 2 == 0 and index != 0:
            print(item)

list_printer()

