#!/usr/bin/python3
""" Creating a functon that add two integers """


def add_integer(a, b=98):
    """ A: first integer, B: second integer """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    """ Adds and returns two integers """
    return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
