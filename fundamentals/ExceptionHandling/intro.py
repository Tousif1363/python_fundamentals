#!usr/bin/env python3

"""
Exception handling is a mechanism for stopping "normal" program flow and
continuing at some surrounding context or code block
"""

"""
Raise an exception to interrupt program flow.

Handle an exception to resume control.

Unhandled exceptions will terminate the program.
"""

"""
Exceptions for programmer error such as IndentationError, SyntaxError, NameError.
You should not normally catch these.
"""

"""
IndexError: when an integer index is out of range
ValueError: when an object is of the right type but contains an inappropriate value
KeyError: Look-up in a mapping fails
"""

"""
EAFP: It's easy to ask for forgiveness than permission
LBYL: Look before you leap

Pythonic: EAFP

EAFP + Exceptions = errors are difficult to ignore!!
"""

"""
Code in the finally block is executed no matter how the try-block exits
"""

"""
Moment of zen:
Errors should never pass silenlty unless explicitly silenced
Errors are like bells and if we make them silent, they are of no use
"""