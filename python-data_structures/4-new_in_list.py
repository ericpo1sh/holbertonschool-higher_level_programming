#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    if idx < 0:
        return my_list

    if idx > len(my_list):
        return my_list

    if my_list:
        templist = my_list.copy()
        templist[idx] = element
        return templist
