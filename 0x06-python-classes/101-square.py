#!/usr/bin/python3
"""Define a Square Class."""

class Square:
    """Square class block"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
    @property
    def size(self):
        return (self.__size)
    @size.setter
    def size (self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @property
    def position(self):
       return (self.__position)
   @poisiton.setter
   def position(self, value):

