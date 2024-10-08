#!/usr/bin/python3
"""Define a class"""


class Square:
    """Represent"""

    def __init__(self, size=0):
        """Initialize"""
        self.size = size

    @property
    def size(self):
        """set the current size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area"""
        return self.__size * self.__size
