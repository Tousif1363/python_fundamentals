#!/usr/bin/env python3

"""
Heterogeneous immutable sequence
"""

"""
Delimiting parantheses are optional for one or more elements
Tuples are useful for multiple return values
"""

a = 3,
print(type(a))
print(a)


def min_max(items):
    return min(items), max(items)


print(min_max([23, 43, 67, 56, 12, 89]))

"""
Tuple unpacking works with arbitrarily nested tuples
"""

(a, (b, (c, d))) = (4, (6, (1, 8)))

print(a, b, c, d)

a = 'jelly'
b = 'bean'

a, b = b, a  # is the idiomatic python swap
print(a, b)

print(tuple([32, 54, 34, 65, 76, 23, 93]))
print(tuple('Hello World!!!'))

"""
Membership test:
    in  :  present in the collection
    not in  :  not present in the collection
"""

print(5 in (3, 5, 7, 'Wassup', 9.6))
