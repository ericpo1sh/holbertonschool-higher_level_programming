#!/usr/bin/python3
""" save_to_json Module """
import json


def save_to_json_file(my_obj, filename):
    """ initializing the function """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
