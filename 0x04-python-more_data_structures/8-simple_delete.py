#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_a_dictionary = {}
    instruction = 0
    for string in a_dictionary:
        if string == key:
            instruction = 1
            continue
        new_a_dictionary.setdefault(string, a_dictionary[string])
    if instruction == 1:
        a_dictionary.pop(key)
    return(new_a_dictionary)
