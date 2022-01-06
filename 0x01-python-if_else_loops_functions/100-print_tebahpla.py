#!/usr/bin/python3
lista = []
lista2 = []
for i in range(97, 123):
    if i % 2 != 0:
        i = i - 32
    lista.append(chr(i))
lista2 = ("".join(lista[:: -1]))
print("{}".format(lista2), end="")
