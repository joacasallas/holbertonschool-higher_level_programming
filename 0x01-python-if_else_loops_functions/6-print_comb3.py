#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i == 8 and j == 9:
            continue
        if j > i:
            print("{}{}".format(i, j), end=", ")
print("{}{}".format(8, 9))
