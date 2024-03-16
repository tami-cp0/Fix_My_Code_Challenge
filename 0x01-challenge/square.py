#!/usr/bin/python3
"""Class Module"""

class Square():
    """Represents a square with methods to calculate its area and perimeter."""

    width = 0

    def __init__(self, width=0, *args, **kwargs):
        self.width = width

    def AreaOfMySquare(self):
        """ Area of the square """
        return self.width * self.width

    def PerimeterOfMySquare(self):
        return (self.width * 4)

    def __str__(self):
        return "{}".format(self.width)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.AreaOfMySquare())
    print(s.PerimeterOfMySquare())
