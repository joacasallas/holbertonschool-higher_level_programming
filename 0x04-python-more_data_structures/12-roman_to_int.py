#!/usr/bin/python3
def roman_to_int(roman_string):
    if len(roman_string) < 1:
        return None
    dictionary = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500,
        'M': 1000,  'zero': 0
    }
    last = 2000
    number = 0
    list_next = []
    for i in range(1, len(roman_string)):
        list_next.append(roman_string[i])
    list_next.append("zero")
    for i in range(len(roman_string)):
        if roman_string[i] in dictionary:
            if dictionary[roman_string[i]] <= last:
                if dictionary[roman_string[i]] < dictionary[list_next[i]]:
                    last = dictionary[roman_string[i]]
                    continue
                else:
                    number += dictionary[roman_string[i]]
                    last = dictionary[roman_string[i]]
            else:
                if dictionary[roman_string[i]] > dictionary[list_next[i]]:
                    previus = dictionary[roman_string[i - 1]]
                    number += (dictionary[roman_string[i]] - previus)
                    last = dictionary[roman_string[i]]
    return number
