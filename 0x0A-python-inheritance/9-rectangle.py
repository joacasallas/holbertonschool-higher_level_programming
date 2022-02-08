#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """method to calculate the area"""
        return self.__width * self.__height

    def __str__(self):
        """magic method to return string of the object"""
        str1 = ("[{}] ".format(self.__class__.__name__))
        str2 = ("{}/{}".format(self.__width, self.__height))
        return str1 + str2
