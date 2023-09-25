#!/usr/bin/python3
""" 1-write_file Module """


def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        f.write(text)
