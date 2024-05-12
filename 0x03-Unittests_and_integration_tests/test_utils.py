#!/usr/bin/env python3
""" module to test utils"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap (unittest.TestCase):
    """ implement test class"""
    @parameterized.expand([
        ("test_01", {"a": 1}, ("a",), 1),
        ("test_02", {"a": {"b": 2}}, ("a",), {'b': 2}),
        ("test_03", {"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, _, a, b, expected):
        """ test case for method access_nested_map"""
        self.assertEqual(access_nested_map(a, b), expected)
