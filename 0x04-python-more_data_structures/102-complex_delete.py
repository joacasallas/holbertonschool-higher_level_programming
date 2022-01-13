#!/usr/bin/bash
def complex_delete(a_dictionary, value):
    new_dictionary = {}
    for key in a_dictionary:
        if a_dictionary[key] != value:
            new_dictionary.setdefault(key, a_dictionary.get(key))
        else:
            continue
    a_dictionary.clear()
    for key in new_dictionary:
        a_dictionary.setdefault(key, new_dictionary.get(key))
    return(a_dictionary)
