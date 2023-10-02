#!/usr/bin/python3
"""
A functoin that adds integers
"""


def add_integer(a, b=98):
    """
    A function that adds two integers
    """
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
