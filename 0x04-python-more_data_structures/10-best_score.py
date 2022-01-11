#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if a_dictionary is None:
        return None
    elif len(a_dictionary) < 1:
        return None
    else:
        for key in a_dictionary:
            value = a_dictionary.get(key)
            if value > max:
                max = value
                keymax = key
            else:
                continue
    return keymax
