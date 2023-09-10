#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for numb in range(0, len(matrix)):
        new_matrix.append(list(map(lambda x: x ** 2, matrix[numb])))
    return new_matrix
