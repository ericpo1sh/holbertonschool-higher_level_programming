#!/bin/usr/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        high = my_list[0]
        for num in my_list:
            if num > high:
                high = num
    return high
