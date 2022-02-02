a = [1, 2, 3, 4]
print(id(a))
a = a + [5]
print(id(a))


a = [1, 2, 3]
print(id(a))
a += [4]
print(id(a))