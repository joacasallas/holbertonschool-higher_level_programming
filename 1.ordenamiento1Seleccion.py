def sortSelection(array):
    length = len(array)
    k = 0
    for i in range(length - 1):
        menor = i
        for j in range (i+1, length):
            k +=1
            print("el ciclo es: {}".format(k))
            if array[j] < array[menor]:
                menor = j
        aux = array[menor]
        array[menor] = array[i]
        array[i] = aux


scores = [2, 7, 3, 1, 4, 0, 6]
print("before ", scores)
sortSelection(scores)
print("after: ", scores)
