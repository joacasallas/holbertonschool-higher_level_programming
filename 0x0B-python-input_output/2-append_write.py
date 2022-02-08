#!/usr/bin/python3
"""Write a function that appends a string at the end of a text
file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a
    file (UTF8) and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
