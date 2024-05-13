#!/usr/bin/env python3
""" module to test client"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """ implement class TestGithubOrgClient"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org_param: str, expected: Dict,
                 mock_json_method: MagicMock) -> None:
        """test method org of class GithubOrgClient"""
        instance = GithubOrgClient(org_param)
        mock_json_method.return_value = expected
        url = instance.ORG_URL
        url = url.replace("{org}", org_param)
        self.assertEquals(instance.org, expected)
        mock_json_method.assert_called_with(url)
