#!/usr/bin/env python3
""" module with one function sum_mixed_list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ function to return sum of list of integers and floats """
    return sum(mxd_lst)
