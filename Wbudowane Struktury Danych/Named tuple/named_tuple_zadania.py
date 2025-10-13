from collections import namedtuple

Apple = namedtuple('Apple',['brand', 'price', 'size'])

apple = Apple('owocowelove', 10, 10)

print(apple.brand, apple.price, apple.size )
print(apple[0], apple[1], apple[2])
for info in apple:
    print(info)