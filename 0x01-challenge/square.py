#!/usr/bin/python3
"""Class Module"""


class Square():
    """Represents a square with methods to calculate its area and perimeter."""

    def __init__(self, width=0, *args, **kwargs):
        if width > 0:
            self.width = width
        else:
            self.width = 0

    def area_of_my_square(self):
        """ Area of the square """
        return (self.width * self.width)

    def perimeter_of_my_square(self):
        """Calculates the perimeter of the square."""
        return (self.width * 4)

    def __str__(self):
        """Returns the width as a string."""
        return "{}".format(self.width)


if __name__ == "__main__":
    s = Square(width=-3)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
