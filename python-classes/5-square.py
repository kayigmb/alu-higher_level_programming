#!/usr/bin/python3
"another class"


class Square:
    "define the class"

    def __init__(self, size=0):
        "calling the variables"
        self.__size = size
        if not isinstance(size, int):
            return TypeError("size must be an integer")
        if size < 0:
            return ValueError("size must be >= 0")

    @property
    def size(self):
        "define the size"
        return self.__size

    @size.setter
    def size(self, value):
        "set values"
        if not isinstance(size, int):
            return TypeError("size must be an integer")
        if size < 0:
            return ValueError("size must be >=0")
        self.__size = value

    def area(self):
        "area"
        return self.__size * self.__size

    def my_print(self):
        "printing"
        if self.__size == 0:
            print()
        for n in range(self.__size):
            print("#" * self.__size)
