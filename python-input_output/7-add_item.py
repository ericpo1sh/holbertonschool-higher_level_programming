#!/usr/bin/python3
""" 7-add_iem.py Module """
from sys import argv
Jsave = __import__('5-save_to_json_file').save_to_json_file
Jload = __import__('6-load_from_json_file').load_from_json_file


try:
    py_list = Jload('add_item.json')
except FileNotFoundError:
    py_list = []
finally:
    Jsave(py_list + argv[1:], 'add_item.json')
