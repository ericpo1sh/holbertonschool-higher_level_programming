#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    for num in my_list:
        if my_list.count(num) == 1:
            total += num
    return total
