#!/usr/bin/env python3

"""
Set is an unordered collection of unique immutable objects
"""

p = {12, 34, 45, 23, 48, 94, 99, 73, 28}

print(p)
print(type(p))

d = {}
print(type(d))

# for an empty set use the set constructor without any arguments

s = set()
print(s)

# duplicates are not allowed in a set

s = set([1, 4, 5, 5, 7, 1, 4, 3, 2, 8, 3, 5, 6, 4])
print(s)

# while iterating a set the order is arbitrary

for x in {1, 2, 4, 8, 16, 32}:
    print(x)

# add elements using the add() method; duplicates are silently ignored

k = {34}
k.add(32)
k.add(21)
k.add(78)
print(k)

k.update([43, 56, 76, 49])
print(k)

# requires the item is present, else it raise a KeyError
k.remove(32)

# discard() method always succeeds
k.discard(43)

print(k)
