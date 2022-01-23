#!/usr/bin/python3
"""write a class Square that defines a square"""


class Square():
    """class that defines a square"""
    def __init__(self, size=0):
        """initializing object
        Args:
        Size: size of square
        Return: Nothing
        """
        self.size = size

    def area(self):
        """method that returns the current square area"""
        return (self.size * self.size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
