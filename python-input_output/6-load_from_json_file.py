#!/usr/bin/python3
""" 6-load_from_json_file Module """
import json


def load_from_json_file(filename):
   """ initializing the function """
   with open(filename, 'r+') as f:
     return json.loads(f)
