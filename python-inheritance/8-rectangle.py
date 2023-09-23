#!/usr/bin/python3
""" Rectangle Module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Initializing the rectangle subclass """

    def __init__(self, width, height):
        """ Validating with integer_validator """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
