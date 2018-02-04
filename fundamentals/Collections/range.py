#!/usr/bin/env python3

"""
Arithmetic progression of integers.
Stop value is one past the end

ranges are "half-open", start is included but stop is not
"""

print(range(5))

for i in range(5):
    print(i)

print(list(range(0, 5)))
print(list(range(5, 10)))

print(list(range(0, 10, 2)))  # here the step is 2

"""
Abusing range
-> Avoid range for iterating over lists
-> Python is not C
-> Don't be un-pythonic!

Prefer direct iteration over iterable objects
"""

"""
Prefer enumerate() for counters
"""

t = [34, 82, 74, 65, 29, 38]

for p in enumerate(t):
    print(p)
