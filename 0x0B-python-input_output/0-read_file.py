#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    try:
        with open(filename, "r") as file:
            for line in file:
                print(line, end="")
            print()
            file.close()
    except FileNotFoundError:
        print("[Errno 2] No such file or directory: '{}'".format(filename))
        exit()
