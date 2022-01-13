#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    above = 0
    under = 0
    for n in my_list:
        above += (n[0] * n[1])
        under += n[1]
    return (above / under)
