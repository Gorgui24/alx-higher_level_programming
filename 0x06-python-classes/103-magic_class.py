#!/usr/bin/python3
"""Define a MagicClass"""

import math
class MagicClass:
    """Represent class"""
    def __init__(self, radius=0):
        """Initialize MagicClass
        Arg:
            radius: (float or int): the radius...
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

        def area(self):
            """Return the area of the MagicClass"""
            return (self.__radius ** 2 * math.pi)

        def circonf(self):
            """Return the circonference of the magic class"""
            return (2 * math.pi * self.__radius)
