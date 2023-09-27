#!/usr/bin/python3
""" This module contains the definition of a Square Class with size."""


class Square:
    """ This is an empty Square Class."""
    def __init__(self, size=0):
        """ Initializes private size attribute."""
        if type(size) is not int:
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must >= 0")
        self.__size = size
