#!/usr/bin/env python3
""" module to test utils"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
)


class TestAccessNestedMap (unittest.TestCase):
    """ implement test class"""
    @parameterized.expand([
        ("test_01", {"a": 1}, ("a",), 1),
        ("test_02", {"a": {"b": 2}}, ("a",), {'b': 2}),
        ("test_03", {"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, _, a: Mapping,
                               b: Sequence, expected: bool) -> bool:
        """ test case for method access_nested_map"""
        self.assertEqual(access_nested_map(a, b), expected)
