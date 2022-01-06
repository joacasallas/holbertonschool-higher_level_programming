#!/usr/bin/python3
def pow(a, b):
    result = 1
    result_temp = 1
    if b < 0:
        b = b * -1
        for i in range(b):
            result_temp *= a
            result = 1 / result_temp
    else:
        for i in range(b):
            result *= a
    return(result)
