

# number_list = [1,2,3,4,5,6,7,8,9,10]
# number_dict = {number:number**2 for number in number_list}
# print(number_dict)


# text = 'banana'
# iter_dict = {letter: text.count(letter) for letter in text}
# print(iter_dict)



dict_keys = ["imię", "wiek", "miasto"]
dicddt_values = ["Kasia", 23, "Warszawa"]
new_dict = {dict_keys[i]: dicddt_values[i] for i in range(len(dict_keys))}
print(new_dict)
new_dict = dict(zip(dict_keys, dicddt_values))
print(new_dict)
