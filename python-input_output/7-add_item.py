#!/usr/bin/python3
import sys
""" 7-add_iem.py """

if __name__ == '__main__':
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    try:
        PythonList = load_from_json_file("add_item.json")
    except FileNotFoundError:
        Pythonlist = []
    save_to_json_file(PythonList + sys.argv[1:], "add_item.json")
