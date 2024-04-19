#!/usr/bin/env python3
""" module  with one function to_kv """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ function to return tuple -item1: string , item2: square"""
    return (k, v ** 2)
