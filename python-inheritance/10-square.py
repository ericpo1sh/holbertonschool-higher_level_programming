#!/usr/bin/python3
""" Square Module """
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Initializing the Square class """

    def __init__(self, size):
        """ Validating with integer_validator """
        super().integer_validator("size", size)
        self.__size = size
    
    def area(self):
        return self.size * self.size
