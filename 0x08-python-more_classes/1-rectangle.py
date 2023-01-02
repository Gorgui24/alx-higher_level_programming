#!/usr/bin/python3
"""Define Rectangle class."""

class Rectangle:
    """Represent a core of class"""
    def __init__(self, width=0, height=0):
        """Initialization

            args:
                width(int): largeur
                height(int): longeur
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Get/Set la largeur du rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Get/Set la longueur du rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
