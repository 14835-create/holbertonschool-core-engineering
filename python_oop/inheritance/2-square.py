#!/usr/bin/env python3
"""Module for square class"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Class reps a square, inherits from rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(width, height)
