#!/usr/bin/python3

"""appends a string at the end of a text file (UTF8)"""
"""number characters"""


def append_write(filename="", text=""):
    """Write a string to a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
