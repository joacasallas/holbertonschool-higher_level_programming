#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py)"""


Rectangle = __import__("9-rectangle").Rectangle
"""importing class Rectangle"""


class Square(Rectangle):
    """class to calculate the square of a number"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
