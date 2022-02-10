#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle"""


from models.rectangle import Rectangle
"""importing class rectangle"""


class Square(Rectangle):
    """class to print a square with '#'"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assing attributes"""
        if args and len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for i, j in kwargs.items():
                setattr(self, i, j)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
