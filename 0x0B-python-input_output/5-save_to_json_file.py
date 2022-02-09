#!/usr/bin/python3
"""Write a function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representatio"""
    with open(filename, "w") as file:
        return json.dump(my_obj, file)
