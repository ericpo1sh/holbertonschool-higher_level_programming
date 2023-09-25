#!/usr/bin/python3
""" Square Module """
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Initializing the Square class """
    pass

    def __init__(self, size):
        """ Validating with integer_validator """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
    def area(self):
        return self.__size ** 2
