#!/usr/bin/python3
""" Base.py Module """
import json


class Base:
    """ Base class initiated """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Attributes initialiazing """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Function that returns dictionary representation """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
