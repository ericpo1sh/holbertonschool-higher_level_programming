#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    templist = my_list.copy()
    if idx < 0:
        return templist

    elif idx > len(my_list) - 1:
        return templist

    if  my_list:
        templist[idx] = element
        return templist
