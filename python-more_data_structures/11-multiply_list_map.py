#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if my_list:
        x = list(map(lambda num: num * number, my_list))
        return x
