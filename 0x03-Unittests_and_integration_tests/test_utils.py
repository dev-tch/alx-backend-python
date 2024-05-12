#!/usr/bin/env python3
""" module to test utils"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any
)


class TestAccessNestedMap (unittest.TestCase):
    """ implement test class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """ test case for method access_nested_map"""
        return self.assertEqual(access_nested_map(nested_map, path), expected)
