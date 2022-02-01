#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle():
    """class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        sendValue = ""
        if self.width == 0 or self.height == 0:
            sendValue = ""
        else:
            for i in range(self.height):
                if i == self.height - 1:
                    sendValue += "#" * self.width
                else:
                    sendValue += "#" * self.width+'\n'
        return sendValue

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
