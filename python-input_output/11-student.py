#!/usr/bin/python3
""" 9-student module """


class Student:
    """ Student Class initiated """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns dictionary representation of a student """
        if type(attrs) is list and all(type(item) == str for item in attrs):
            new_dict = {}
            for aTT in attrs:
                if hasattr(self, aTT):
                    new_dict[aTT] = getattr(self, aTT)
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            self.__dict__[key] = value
