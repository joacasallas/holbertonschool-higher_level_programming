def sortBurbuja(array):
    lenght = len(array)
    k = 0
    for i in range (lenght - 1):
        k +=1
        print("el ciclo es: {}".format(k))
        for j in range (lenght - 1):
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux


scores = [2, 7, 3, 1, 4, 0, 6]
print("before ", scores)
sortBurbuja(scores)
print("after: ", scores)
