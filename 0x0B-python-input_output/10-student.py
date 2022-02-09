#!/usr/bin/python3
"""
Definning a class Student.
"""


class Student:
    """
    Student representation.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializing student class.
        Arguments:
            first_name (str): Student's first name.
            last_name  (str): Student's Last name.
            age       (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        dictionary Student's representation.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
