#!/usr/bin/python3
""" function that adds 2 numbers """


def add_integer(a, b=98):
    """ function that adds 2 numbers """
    if type(a) == str:
        raise TypeError("a must be an integer")
    elif type(b) == str:
        raise TypeError("b must be an integer")
    elif a is None:
        raise TypeError("a must be an integer")
    else:
        return int(a) + int(b)
