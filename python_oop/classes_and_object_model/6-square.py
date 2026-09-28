#!/usr/bin/env python3
"""Defines a square class with size, position, and printing."""


class Square:
    """Reps a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position of square with validation"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(n, int) for n in value)
            or not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with # characters using position"""
        if self.__size == 0:
            print("")
            return

        print("\n" * self.__position[1], end="")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

        return "".join(lines).rstrip()
