from collections import namedtuple

Location = namedtuple('Location',['latitude','longitude'])

location = Location(1, 2)
print(location)
print(location.latitude, location.longitude)
print(type(location))