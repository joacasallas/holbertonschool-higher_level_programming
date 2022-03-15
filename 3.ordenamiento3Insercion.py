def sort3Insercion(array):
    length = len(array)
    k = 0
    for i in range(length - 1):
        k +=1
        print("el ciclo es: {}".format(k))
        for j in range(length - 1):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
                if array[j] < array[j - 1]:
                    aux = array[j - 1]
                    array[j - 1] = array[j]
                    array[j] = aux

scores = [2, 7, 3, 1, 4, 0, 6]
print("before ", scores)
sort3Insercion(scores)
print("after: ", scores)