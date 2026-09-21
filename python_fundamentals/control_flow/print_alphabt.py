#!/usr/bin/env python3
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("{}".format("".join(c for c in alphabet if c not in ("q", "e"))), end ="")
