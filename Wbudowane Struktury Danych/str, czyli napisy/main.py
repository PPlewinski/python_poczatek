
# zbigniew_stonoga = ['dsda', 'dada', 'dad2s']
# print(zbigniew_stonoga)
# print("".join(zbigniew_stonoga))

# name = "     Paweł      "
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())

# name = " ./ Paweł >/"
# print(name.strip("./"))

last_name = "Plewiński"
print(last_name.startswith("Plewi"))
print(last_name.endswith("ński"))

# number = 123
# print(str(number).zfill(3))


# zdanie = "Joł Joł Joł jestem Jowisz"
# print(zdanie.find('Joł'))
# print(zdanie.index('Joł'))
# print(zdanie.index('Joł', 6, 15))
# print(zdanie.find('dsadsa'))
# print(zdanie.index('dsadsa'))


p = 'Python'
age = 30
message = "{p} ma już ponad {age} lat".format(age=age,p=p)
print(message)
message = "%s ma już ponad %d lat" % (p,age)
print(message)
print(message)