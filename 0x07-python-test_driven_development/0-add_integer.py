#!/usr/bin/python3
""" function that adds 2 numbers """


def add_integer(a, b=98):
    """ function that adds 2 numbers """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    elif b is None or (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
