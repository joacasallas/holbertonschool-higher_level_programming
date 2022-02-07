#!/usr/bin/python3
"""creation class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """method to order list"""
        print(sorted(list(self)))
