#!/usr/bin/env python3

import time


def print_time(t=time.ctime()):
    print(t)


"""
Default arguments are evaluated when def is evaluated
Can be a confusing trap for the unwary that usually shows up in using mutable collections as argument defaults
"""


def add_spam(breakfast=[]):  # using a mutable object as default argument
    breakfast.append('spam')
    print(breakfast)


def add_spam_better(breakfast=None): # using an immutable object as the default argument
    if breakfast is None:
        breakfast = []
        breakfast.append('spam')
    print(breakfast)
