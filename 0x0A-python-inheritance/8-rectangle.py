#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """ Initialization"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._width = width
        self. height = height
