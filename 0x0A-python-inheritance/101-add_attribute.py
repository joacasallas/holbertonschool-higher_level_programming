#!/usr/bin/python3
"""Write a function that adds a new attribute to an object"""


def add_attribute(objet, name, value):
    """Write a function that adds a new attribute to an object"""
    if not hasattr(objet, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(objet, name, value)
