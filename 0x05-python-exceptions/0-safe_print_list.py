#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for n in my_list:
        try:
            if i < x:
                print("{}".format(n), end="")
                i += 1
        except IndexError:
            break
    print("")
    return i
