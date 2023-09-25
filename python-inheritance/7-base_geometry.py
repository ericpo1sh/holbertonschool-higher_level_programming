#!/usr/bin/python3
""" BaseGeometry Module """


class BaseGeometry:
    """ Write a class BaseGeometry. """

    def area(self):
        """ initializing area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Checking Errors """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
