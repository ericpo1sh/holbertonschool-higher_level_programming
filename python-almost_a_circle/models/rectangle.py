#!/usr/bin/python3
""" Rectangle Module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class initiated """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor Parameters and Attributes Created """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Setting width return """
        return self.__width

    @width.setter
    def width(self, width):
        """ Initializing characteristics of widh """
        self.__width = width

    @property
    def height(self):
        """ Setting height return """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setting characteristics of height """
        self.height = height

    @property
    def x(self):
        """ Setting return for x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setting characteristics for x """
        self.__x = x

    @property
    def y(self):
        """ setting return for x """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setting characteristics of y """
        self.__y = y
