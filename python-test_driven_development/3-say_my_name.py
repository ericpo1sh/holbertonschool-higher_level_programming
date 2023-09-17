#!/usr/bin/python3
""" Making a function that prints first and last name """


def say_my_name(first_name, last_name=""):
    """ Checking if first name is a valid string """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    """ Checking if last name is a valid string """
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    """ Printing result """
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
