#!/usr/bin/python3
""" 0-read_file Module """


def read_file(filename=""):
    """ initializing function """
    with open(filename, 'r') as f:
        for line in f:
            print(line, end="")
