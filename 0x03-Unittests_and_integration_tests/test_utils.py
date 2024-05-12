#!/usr/bin/env python3
""" module to test utils"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import (
    Dict,
    Tuple,
    Union
)


class TestAccessNestedMap (unittest.TestCase):
    """ implement test class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, a: Dict, b: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """ test case for method access_nested_map"""
        self.assertEqual(access_nested_map(a, b), expected)
