#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Initializing constructor """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializing class Methods/Attributes """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ function to return string """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))
