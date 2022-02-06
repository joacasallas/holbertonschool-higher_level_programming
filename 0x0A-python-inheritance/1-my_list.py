#!/usr/bin/python3
"""creation class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""
    pass

    def print_sorted(self):
        """method to order list"""

        new = sorted(list(self))
        return new
