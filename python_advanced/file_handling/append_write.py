#!/usr/bin/env python3
"""Module appends string at the end of txt file"""


def append_write(filename="", text=""):
    """Append a string to UTF-8 txt file and return chars addded."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
