#!/usr/bin/env python3
"""Module writes string to txt file."""


def write_file(filename="", text=""):
    """Write string to txt file and return num of chars written."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
