#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for row in range(0, len(matrix)):
            for numb in range(0, len(matrix[row])):
                if numb == len(matrix[row]) - 1:
                    print("{:d}".format(matrix[row][numb]))
                else:
                    print("{:d}".format(matrix[row][numb]), end=" ")
