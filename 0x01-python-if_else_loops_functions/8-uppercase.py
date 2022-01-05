#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) in range(97, 123):
            ascci_code = (ord(i)-32)
            character = chr(ascci_code)
        else:
            character = i
        print("{}".format(character), end="")
    print("")
