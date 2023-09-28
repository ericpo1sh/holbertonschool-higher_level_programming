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
        self.__width = value

    @property
    def height(self):
        """ Setting height return """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting characteristics of height """
        self.__height = value

    @property
    def x(self):
        """ Setting return for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setting characteristics for x """
        self.__x = value

    @property
    def y(self):
        """ setting return for x """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setting characteristics of y """
        self.__y = value
