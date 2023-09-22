#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Rectangle Module """


class Rectangle(BaseGeometry):
    """ Initializing the rectangle class """
    def __init__(self, width, height):
        """ Validating with integer_validator """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
