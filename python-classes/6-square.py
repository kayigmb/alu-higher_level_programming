#!/usr/bin/python3
"class module"


class Square:
    """define a class"""

    def __init__(self, size=0, position=(0, 0)):
        "intialize the class"
        self.size = size
        self.position = position

    @property
    def size(self):
        "size"
        return self.__size

    @size.setter
    def size(self, value):
        "define the size"
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        "position"
        return self.__position

    @position.setter
    def position(self, value):
        "classes"
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        "area"
        return self.__size**2

    def my_print(self):
        "classes"
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
