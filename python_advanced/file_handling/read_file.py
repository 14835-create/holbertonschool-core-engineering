#!/usr/bin/env python3
"""Module reads file and prints stdout."""

def read_file(filename=""):
    """Read UTF-8 text file amd print stdout."""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
