#!/usr/bin/env python3

"""
Unordered mapping from unique, immutable keys to mutable values

keys must be immutable
values must be mutable
The dictionary itself is mutable

"""

house = {'kitchen': 56, 'master-bedroom': 140, 'bathroom': 34}

print(house)

house['terrace'] = 250
house['bedroom'] = 100

print(house)

for roomType in house:
    print(roomType, house[roomType])
#    print(roomType + " " + str(house[roomType]))

"""
dict() constructor accepts:
->  iterable series of key-value 2-tuples
->  keyword arguments - requires keys are valid python identifiers  
"""
names_and_ages = [('Alice', 32), ('Roman', 43), ('Bob', 35), ('Louis', 23)]
d = dict(names_and_ages)
print(d)

phonetic = dict(a='alpha', b='bravo', c='charlie')
print(phonetic)

e = d.copy()

f = dict(e)

phonetic.update(dict(d='delta', e='echo', f='foxtrot'))
print(phonetic)

phonetic.update(dict(e='ess'))
print(phonetic)

"""Dictionary iteration is over keys. Order is arbitrary"""

for alpha in phonetic:
    print("{a} is {b}".format(a=alpha, b=phonetic[alpha]))

# to iterate over values in a dictionary

for sounds in phonetic.values():
    print(sounds)

# to iterate over keys and values in a dictionary

for key, value in phonetic.items():
    print(key, value)

import pprint

pprint.pprint(phonetic)
