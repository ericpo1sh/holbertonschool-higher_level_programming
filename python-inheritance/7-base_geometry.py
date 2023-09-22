#!/usr/bin/python3
""" BaseGeometry Module """


class BaseGeometry:
    """ Write a class BaseGeometry. """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be a integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
