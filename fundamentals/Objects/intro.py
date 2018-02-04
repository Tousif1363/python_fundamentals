#!/usr/bin/env python3

a = 34
b = 56

print(id(a))
print(id(b))

b = a
print(id(a))
print(id(b))

print(id(a) == id(b))
print(a is b)

b += 3  # the assignment operator only binds to names, it never copies an object by value
print(id(b))

b = 12
print(id(b))

"""Python does not have variables in the metaphorical sense, as in a box holding a value
    It only has named references to objects and references behave like labels which allow us to 
    retrieve objects
"""

p = [2, 3, 4]
q = [2, 3, 4]

print(p == q)  # value equality: equivalent contents; can be controlled programatically
print(p is q)  # identity: same object; defined by the language and you cannot change that behavior


