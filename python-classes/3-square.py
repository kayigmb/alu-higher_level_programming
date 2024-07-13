#!/usr/bin/python3
"another square clss"


class Square:
    "another class definition"

    def __init__(self, size=0):
        "define the clase"
        self._size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        "calculate"
        return self._size**2
