#!/usr/bin/python3
""" Creating an empty class called rectangle """


class Rectangle:
    """ Rectangle class initiated """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Setting attributes of Rectangle """
        type(self).number_of_instances += 1
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
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Checks area difference and returns higher rect """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
        
    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __str__(self):
        """ Making the print function """
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for x in range(self.__width):
                print(self.print_symbol, end="")
            if i != self.__height - 1:
                print()
        return ""

    def __repr__(self):
        """ Defining repr function """
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height)\
            + ")"

    def __del__(self):
        """ Defining del function """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
