#!/usr/bin/python3
""" Creating a function that indents text """


def text_indentation(text):
    """ Checking if str is a string, If not Raise Error """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    """ Deliminators for loop """
    for deli in ".?:":
        text = (deli + "\n\n").join(
            [line.strip(" ") for line in text.split(deli)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("test/5-test_indentation.txt")
