#!/usr/bin/python3
""" 2-append_write Module """


def append_write(filename="", text=""):
    """ initializing the append_write function """
    if not open(filename, 'r'):
        with open(filename, 'xa') as f:
            f.write(text)
    return f.write(text)
