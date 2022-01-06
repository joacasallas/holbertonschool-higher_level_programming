#!/usr/bin/python3
j = -25
for i in range(97, 123):
    i = i - j
    j = j + 2
    if i % 2 != 0:
        i = i - 32
    print("{}".format(chr(i)), end="")
