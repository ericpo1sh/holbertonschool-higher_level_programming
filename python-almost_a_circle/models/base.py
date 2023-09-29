#!/usr/bin/python3
""" Base.py Module """
import json
import sys


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
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Function that writes the JSON string rep of list to file """
        with open(cls.__name__ + ".json", 'w') as f:
            empty_list = []
            if list_objs is None:
                pass
            else:
                for obj in list_objs:
                    empty_list.append(obj.to_dictionary())
            f.write(Base.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """ Function that returns the list of JSON string reps """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Function that returns instances of all attributes """
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1, 1)
        elif cls.__name__ == "Sqaure":
            dum = cls(1, 1, 1)
        dum.update(**dictionary)
        return dum
