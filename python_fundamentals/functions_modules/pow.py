#!/usr/bin/env python3
def pow(a, b):
    b = int(b)
    result = 1
    for _ in range(b):
        result *= a
        print(result, end="")
        return result
