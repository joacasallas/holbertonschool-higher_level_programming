#!/usr/bin/python3
"""Write a class MyInt that inherits from int"""


class MyInt(int):
    """Write a class MyInt that inherits from int"""
    def __init__(self, number):
        """initialization"""
        self.number = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if type(number) != int:
            raise ValueError("number must be an integer")
        else:
            self.__number = number

    def __eq__(self, other):
        if self.__number == other:
            return False
        else:
            return True

    def __ne__(self, other):
        if self.number != other:
            return False
        else:
            return True
