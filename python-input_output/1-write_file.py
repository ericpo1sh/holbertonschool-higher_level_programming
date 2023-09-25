#!/usr/bin/python3
""" 1-write_file Module """


def write_file(filename="", text=""):
    """ Initializing the write file function """
    with open(filename, 'w') as f:
        return f.write(text)
