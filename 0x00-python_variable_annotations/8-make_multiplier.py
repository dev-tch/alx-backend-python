#!/usr/bin/env python3
"""module with one function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return callable function"""
    def multiply(x: float) -> float:
        """ multiplication function  """
        return (x * multiplier)
    return multiply
