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
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Test access_nested_map method"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
