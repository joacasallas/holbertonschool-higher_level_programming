#!/usr/bin/python3
def roman_to_int(roman_string):
    if len(roman_string) < 1:
        return None
    dictionary = {
        'I' : 1, 'V' : 5, 'X' : 10, 
        'L' : 50, 'C' : 100, 'D' : 500, 
        'M' : 1000
    }
    number = 0
    last = 2000
    for n in roman_string:
        if n in dictionary:
            if int(dictionary[n]) > last:
                number = int(dictionary[n]) - number
            else:
                number += int(dictionary[n])
            last = int(dictionary[n])
            #number += int(dictionary[n])
    return number
