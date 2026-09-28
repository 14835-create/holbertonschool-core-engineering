#!/usr/bin/env python3
"""Defines a square class with size validation and printing."""


class Square:
    """Reps a square"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Gets size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size of square with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with # characters"""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
