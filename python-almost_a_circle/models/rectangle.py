#!/usr/bin/python3
""" Rectangle Module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class initiated """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor Parameters and Attributes Created """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Setting width return """
        return self.__width

    @width.setter
    def width(self, value):
        """ Initializing characteristics of widh """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Setting height return """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting characteristics of height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Setting return for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setting characteristics for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ setting return for x """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setting characteristics of y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ Setting return for area """
        return self.__width * self.__height

    def display(self):
        """ Displats # character for rectangle area """
        for hite in range(self.__height):
            for wdth in range(self.__width):
                print("#", end="")
            print()
