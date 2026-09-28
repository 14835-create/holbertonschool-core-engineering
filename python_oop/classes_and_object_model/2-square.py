#!/usr/bin/env python3
"""Defines Square class with size validation"""


class Square:
    """Reps a square with a private size"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
