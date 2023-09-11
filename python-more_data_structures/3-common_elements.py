#!/usr/bin/python3

def common_elements(set_1, set_2):
    for item in set_1:
        for items in set_2:
            if item == items:
                set_3 = item
    return set_3

