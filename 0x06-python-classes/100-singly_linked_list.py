#!/usr/bin/python3
"""Define classe for linked list"""

class Node:
    """Represent a node singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize
        args:
            data: (int) : int
            next_node ((Node): int
        """
        self.data = data
        self.next_nextnode = next_node

    @property
    def data(self):
        """Getter and setter"""
        return (self.__data)
    @data.setter
    def data(self, value):
        for not isinstance(value, int):
            raise TypeError("ata must be an integer")
        self.__data = value
    @property
    def next_node(self, value):
        return (self.__next_node)
    @next_node.setter


