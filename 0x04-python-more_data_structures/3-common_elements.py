#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for string in set_1:
        if string in set_2:
            new_set.add(string)
        else:
            continue
    return new_set
