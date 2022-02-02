#!/usr/bin/python3
"""modul"""


class Student():
    """class"""

    def __init__(self, first_name, last_name, age):
        """inizilitation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dicti"""
        return self.__dict__
