#!/usr/bin/env python3
"""Defines square class that ingerits from rectangle"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Reps a square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
