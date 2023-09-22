#!/usr/bin/python3
""" Rectangle Module """


class BaseGeometry:
    """ Write a class BaseGeometry. """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be a integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ Initializing the rectangle class """
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
