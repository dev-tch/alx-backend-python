#!/usr/bin/env python3
""" module with one function safe_first_element"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ return union from sequence"""
    if lst:
        return lst[0]
    else:
        return None
