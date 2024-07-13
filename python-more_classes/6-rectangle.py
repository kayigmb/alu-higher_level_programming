#!/usr/bin/python3
"""import """


class Rectangle:
    """creating"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialization"""

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting the value"""
        return self.__width

    @width.setter
    def width(self, value):
        "width"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting the value"""
        return self.__height

    @height.setter
    def height(self, value):
        "height"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculating and returning"""
        return self.__width * self.__height

    def perimeter(self):
        """calculating"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """print"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Return the string"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """Print"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
