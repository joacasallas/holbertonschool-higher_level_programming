#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for string in set_1:
        if string in set_2:
            continue
        else:
            new_set.add(string)
    for string in set_2:
        if string in set_1:
            continue
        else:
            new_set.add(string)
    return new_set
