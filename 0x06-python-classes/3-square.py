#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square():
    """class that defines a square"""
    def __init__(self, size=0):
        """initializing object
        Args:
        Size: size of square
        Return: Nothing
        """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """method that returns the current square area"""
        area = self.__size * self.__size
        return area
