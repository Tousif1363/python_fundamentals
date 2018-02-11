#!usr/bin/env python3

"""
A protocol is a set of operations that a collection or type must support
if it is to implement that protocol

container : Membership test using in and not in
sized: size can be determined by passing the type to the built-in len(s) function
iterable: can produce an iterator with iter(s), gives element one by one as requested. can be used with for loops
------------
str, list, dict, bytes, set, tuple, range

sequence:
retrieve the elements using index; item = seq[index]
find items by value; index = seq.index(value)
find the count of an item = seq.count(value)
a reverse sequence can be produced using the reversed() function
------------
str, list, range, tuple, bytes

mutable sequence
------------
list

mutable set
------------
set

mutable mapping
------------
dict
"""