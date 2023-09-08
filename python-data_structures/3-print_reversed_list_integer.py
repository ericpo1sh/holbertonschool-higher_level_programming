#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for item in range(len(my_list) - 1, 0):
        print("{:d}".format(item))
