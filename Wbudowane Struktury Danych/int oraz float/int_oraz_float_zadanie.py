import random
import math

lista_liczb = []
for _ in range (6):
    lista_liczb.append(random.uniform(-20,20))

lista_liczb_cal = []
for _ in range (3):
    lista_liczb_cal.append(random.randint(1,10))

print(lista_liczb_cal)
print(lista_liczb)

print(round(lista_liczb[0]))
print(math.ceil(lista_liczb[1]))
print(math.floor(lista_liczb[2]))

print(pow(lista_liczb[3],lista_liczb_cal[0]))
print(pow(lista_liczb[4],lista_liczb_cal[1]))
print(pow(lista_liczb[5],lista_liczb_cal[2]))