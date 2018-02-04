#!/usr/bin/env python3

f = [1, 2, 3]


def append_value_to_list(g):
    g.append(4)


def assign_list(g):
    g = [7, 8, 9]


def replace_content(g):
    g[0] = 12
    g[1] = 13
    g[2] = 14
    g[3] = 15


append_value_to_list(f)
print(f)

assign_list(f)
print(f)

replace_content(f)
print(f)

"""
Pass by object reference
    The value of the reference is copied, not the value of the object
"""


def func(g):
    return g


print(f is func(f))
