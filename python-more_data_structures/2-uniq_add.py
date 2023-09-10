#!/usr/bin/python3

def uniq_add(my_list=[]):
    total = 0
    single_list = []
    for num in sorted(set(my_list)):
        single_list.append(num)
    for num in single_list:
        total += num
    return total
