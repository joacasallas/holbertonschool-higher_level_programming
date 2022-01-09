#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) < 1:
        exit
    else:
        for i in range(len(my_list)):
            print("{:d}".format(my_list[len(my_list)-1-i]))
