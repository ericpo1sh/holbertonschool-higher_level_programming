#!/usr/bin/python3
""" 1-write_file Module """


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
