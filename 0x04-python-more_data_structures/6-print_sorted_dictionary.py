#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary_sorted = sorted(a_dictionary)
    for key in a_dictionary_sorted:
        print("{}: {}".format(key, a_dictionary.get(key)))
