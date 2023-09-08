#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        templist = my_list.copy()
        if idx < 0:
            return templist

        elif idx > len(my_list) - 1:
            return templist

        else:
            templist[idx] = element
            return templist
