#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for n in my_list:
        if i <= (x - 1):
            print("{}".format(n), end="")
            i += 1
    print("")
    return i
