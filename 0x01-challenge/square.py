#!/usr/bin/python3
"""Class Module"""

class square():
    """Represents a square with methods to calculate its area and perimeter."""

    width = 0

    def __init__(self, width=0, *args, **kwargs):
        self.width = width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PerimeterOfMySquare(self):
        return (self.width * 4)

    def __str__(self):
        return "{}".format(self.width)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PerimeterOfMySquare())
