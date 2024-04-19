#!/usr/bin/env python3
""" module with one function floor"""


def floor(n: float) -> int:
    """function to return the floor of float"""
    if (n >= 0):
        return int(n)
    else:
        return int(n - 1)
