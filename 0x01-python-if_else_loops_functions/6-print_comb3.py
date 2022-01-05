#!/usr/bin/python3
list_num = []
for i in range(10):
    for j in range(10):
        if i == j:
            continue
        num_str = (str(i)+str(j))
        num_str_rev = (str(j)+str(i))
        if num_str_rev in list_num:
            continue
        list_num.append(num_str)
print(", ".join(list_num))
