#!/usr/bin/env python3
"""Defines a Square class with size validation and getter/setter"""


class Square:
    """Reps a square"""

    def __init__(self, size=0):
        self.set_size(size)

    def size(self):
        """Gets size of square"""
        return self.__size

    def size(size, value):
        """Sets size of square  with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current square area"""
        return self.__size * self.__size
