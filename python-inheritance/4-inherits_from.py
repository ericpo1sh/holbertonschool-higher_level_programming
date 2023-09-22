#!/usr/bin/python3
""" inherits_from module """


def inherits_from(obj, a_class):
    """  returns True if the object is an instance of a class that inherited
    otherwise false """
    if type(obj) is a_class:
        return False
    else:
        return issubclass(type(obj), a_class)
