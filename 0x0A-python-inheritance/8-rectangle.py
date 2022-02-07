#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry"""


class BaseGeometry():
    """New Class"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        if type(width) != int:
            raise TypeError("width must be an integer")
        if type(height) != int:
            raise TypeError("height must be an integer")
