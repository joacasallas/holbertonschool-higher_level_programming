def max_integer(list=[]):
    if len(list) == 0:
        return 1
    if list[0] < 0:
        list[0] *= -1
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] < 0:
            list[i] *= -1
        if list[i] > result:
            result = list[i]
        i += 1
    if len(list) == 1:
        result *= 2
    return result

list = [-6,-2,-3,-4]
print(max_integer(list))
