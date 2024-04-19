#!/usr/bin/env python3
""" module with one function sum_list """
import functools


def sum_list(input_list: list[float]) -> float:
    """ count sum of list elements """
    return functools.reduce(lambda x, y: x + y, input_list)
