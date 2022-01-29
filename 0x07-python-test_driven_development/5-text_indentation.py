#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of \
these characters: ., ? and :"""


def text_indentation(text):
    """function that prints a text with 2 new lines \
    after each of these characters: ., ? and :"""
    if type(text) != str:
        raise TypeError("text must be a string")
    position_character = 0
    for character in text:
        if position_character == 0:
            if character == " ":
                continue
            else:
                position_character = 1
        if position_character == 1:
            if character == "?" or character == ":" or character == ".":
                print(character)
                print()
                position_character = 0
            else:
                print(character, end="")
