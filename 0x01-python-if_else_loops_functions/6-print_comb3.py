#!/usr/bin/python3
list_num = []
for i in range(10):
    for j in range(10):
        if i == j:
            continue
        num_pair = i, j
        num_pair_rev = j, i
        if num_pair_rev in list_num:
            continue
        list_num.append(num_pair)
        if i == 8 and j == 9:
            continue
        print("{}{}, ".format(i, j), end="")
print("{}{}".format(8, 9))
