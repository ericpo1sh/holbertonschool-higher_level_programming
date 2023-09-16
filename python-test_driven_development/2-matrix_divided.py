#!/usr/bin/python3
""" Creating function that divides matrix by int """


def matrix_divided(matrix, div):
    """ Checking if div arg is 0 """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    """ Checking if div is a int or a float """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            """ Checking if items in row are ints/floats """
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            """ Checking size of row is equal """
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                """ Checking if each item is a float/integer """
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/2-matrix_divided.txt")
