#!/usr/bin/python3
""" 7-add_item.py Module """
from sys import argv
import json
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


try:
    py_list = load('add_item.json')
except FileNotFoundError:
    py_list = []
finally:
    save(py_list + argv[1:], 'add_item.json')
