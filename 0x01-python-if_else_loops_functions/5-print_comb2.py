#!/usr/bin/python3
def print_num():
    for i in range(99):
        if i < 10:
            print("0{}, ".format(i), end="")
        else:
            print("{}, ".format(i), end="")


print_num()
print(99)
