#!/usr/bin/python3
"comment"
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    "comment"

    def __init__(self, size):
        "comment"
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
