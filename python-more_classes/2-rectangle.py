#!/usr/bin/python3
""" Creating an empty class called rectangle """


class Rectangle:
    """ Rectangle class initiated """
    def __init__(self, width=0, height=0):
        """ Setting attributes of Rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Setting property for width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Defining characteristics of wdith """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """ Setting property for height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Defining characteristics of height """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        """ Returns width times height """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter for the rectangle """
        if height == 0 or width == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)
