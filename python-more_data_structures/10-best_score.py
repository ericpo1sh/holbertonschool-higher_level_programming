#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    highval = None
    for key, value in a_dictionary.items():
        if highval is None or value > highval:
            highval = value
            highname = key
    return highname
