# mutable mappings of keys to values

house = {'kitchen': 56, 'master-bedroom': 140, 'bathroom': 34}

print(house)

house['terrace'] = 250
house['bedroom'] = 100

print(house)

for roomType in house:
    print(roomType, house[roomType])
#    print(roomType + " " + str(house[roomType]))
