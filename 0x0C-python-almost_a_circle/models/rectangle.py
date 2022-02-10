#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""


from models.base import Base
"""importing class Base"""


class Rectangle(Base):
    """subclass Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("value must be > 0")
        if type(value) != int:
            raise TypeError("value must be an integer")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("value must be > 0")
        if type(value) != int:
            raise TypeError("value must be an integer")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value <= 0:
            raise ValueError("value must be > 0")
        if type(value) != int:
            raise TypeError("value must be an integer")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value <= 0:
            raise ValueError("value must be > 0")
        if type(value) != int:
            raise TypeError("value must be an integer")
        self.__y = value
