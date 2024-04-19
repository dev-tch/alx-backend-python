#!/usr/bin/env python3
"""module with one function element_length"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return list of elements with length"""
    return [(i, len(i)) for i in lst]
