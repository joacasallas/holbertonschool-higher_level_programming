#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = (str[:n]+str[n+1:])
    if n < 0:
        str2 = str
    return(str2)
