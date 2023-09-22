#!/usr/bin/python3
""" Rectangle Module """


class BaseGeometry:
    """ Write a class BaseGeometry. """
    def area(self):
        """ initializing area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Checking Errors """
        if type(value) is not int:
            raise TypeError("{} must be a integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ Initializing the rectangle class """

    def __init__(self, width, height):
        """ Validating with integer_validator """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
