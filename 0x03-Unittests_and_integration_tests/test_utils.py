#!/usr/bin/env python3
""" module to test utils"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ implement test class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map method"""
        output = access_nested_map(nested_map, path)
        self.assertEqual(output, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, except_error):
        """test case of raising execption when try to acces unknown key"""
        with self.assertRaises(except_error):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """implement class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """ Mock HTTP calls"""
        attrs = {'json.return_value': test_payload}
        with patch('requests.get', return_value=Mock(**attrs)) as mock_request:
            self.assertEquals(get_json(test_url), test_payload)
            mock_request.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ implement class TestMemoize"""
    def test_memoize(self):
        """ Parameterize and patch"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=lambda: 42) as mock_method:
            instance = TestClass()
            instance.a_property()
            self.assertEquals(instance.a_property(), 42)
            self.assertEquals(instance.a_property(), 42)
            mock_method.assert_called_once()
