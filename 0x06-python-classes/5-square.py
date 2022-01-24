#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square():
    """define a square"""
    def __init__(self, size=0):
        """initialization object
        Args:
        size: size of the sauqre
        Return: Nothing
        """
        self.size = size

    def area(self):
        """public method to return area od square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """definition property size to call value"""
        return self.__size

    @size.setter
    def size(self, value):
        """definition setter size to edit value"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """public method to print with '#' the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("{}".format("#"), end="")
                print()
