#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [None] * len(my_list)
    for num in my_list:
        if my_list[num] % 2 == 0:
            new_list[num].append(True)
        else:
            new_list[num].append(False)
    return new_list
