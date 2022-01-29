#!/usr/bin/python3
"""function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    new = []
    errormessage = "matrix must be a matrix (list of lists) of integers/floats"

    """function that divides all elements of a matrix."""
    if div is None or (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError(errormessage)
    for list2 in matrix:
        if type(list2) != list: or len(list2) == 0;
            raise TypeError(errormessage)
        if len(list2) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new = [[round((item / div), 2) for item in list2] for list2 in matrix]
    return new
