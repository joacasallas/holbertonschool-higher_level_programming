#!/usr/bin/python3
def max_integer(my_list=[1, 9, 2, 82, 5]):
    if len(my_list) == 0:
        return None
    else:
        max = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > max:
                max = my_list[i]
            else:
                continue
    return max
