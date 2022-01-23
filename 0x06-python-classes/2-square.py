#!/usr/bin/python3
"""Define a class Square"""


class Square():
    """Define a class Square"""
    def __init__(self, size=0):
        """initializes the square
        Args:
        size: size of the square
        Return: Nothing
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
