#!/usr/bin/env python3
"""Defines Square class with size validation"""


class Square:
    """Reps a Square"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Return area of the Square"""
            return self._size * self.__size
