#!/usr/bin/python3
""" Creating a print square functiomn """


def print_square(size):
    """ Method for printing a square with n characters.

    Size: int representing size of the square.

    Raises: TypeError, ValueError.

    """
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    for i in range(size):
        for x in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/4-print_square.txt")
