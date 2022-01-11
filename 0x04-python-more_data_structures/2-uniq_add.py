#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    run = 0
    for n in my_list:
        if n in my_list[:run]:
            continue
        else:
            sum += n
            run += 1
    return sum
