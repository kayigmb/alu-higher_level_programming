#!/usr/bin/python3
"""import any modulie just Defines a Rectangle class"""


class Rectangle:
    """Representation"""

    def __init__(self, width=0, height=0):
        """Initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """setting"""
        return self.__width

    @width.setter
    def width(self, value):
        "instance"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting"""
        return self.__height

    @height.setter
    def height(self, value):
        "height"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
