#!/usr/bin/python3
""" Creating an empty class called rectangle """


class Rectangle:
    """ Rectangle class initiated """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise TypeError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise TypeError("heigh tmust be >= 0")
        self.__height = height
