#!/usr/bin/python3
""" Rectangle Module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Initializing the rectangle class """

    def __init__(self, width, height):
        """ Validating with integer_validator """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __repr__(self):
        """ Print function that displays x/y """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
