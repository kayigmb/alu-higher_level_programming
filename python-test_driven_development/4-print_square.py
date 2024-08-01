#!/usr/bin/python3
"""
comment
"""


def print_square(size):
    """
    comment
    """
    square = ""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for c in range(size):
        square += "#" * size + "\n"
    print(square, end="")
