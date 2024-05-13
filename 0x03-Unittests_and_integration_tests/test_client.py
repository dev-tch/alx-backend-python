#!/usr/bin/env python3
""" module to test client"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, MagicMock, PropertyMock, Mock
from client import GithubOrgClient
from typing import Dict
from fixtures import TEST_PAYLOAD
from requests import HTTPError


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

    def test_public_repos_url(self):
        """ test method _public_repos_url"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_prop_org:
            repo_url = "https://api.github.com/users/google/repos"
            mock_prop_org.return_value = {
                'repos_url': repo_url,
            }
            instance = GithubOrgClient("google")
            self.assertEquals(instance._public_repos_url, repo_url)

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """ test function public_repos of client module"""
        json_org_google = {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "url": "https://api.github.com/orgs/google",
            "repos_url": "https://api.github.com/orgs/google/repos",
            "events_url": "https://api.github.com/orgs/google/events",
            "type": "Organization"
        }
        json_repos_url = [
            {
                "id": 1936771,
                "node_id": "MDEwOlJlcG9zaXRvcnkxOTM2Nzcx",
                "name": "truth",
                "full_name": "google/truth",
            },
            {
                "id": 3248531,
                "node_id": "MDEwOlJlcG9zaXRvcnkzMjQ4NTMx",
                "name": "autoparse",
            },
            ]
        mock_json.return_value = json_repos_url
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repo:
            mock_repo.return_value = json_org_google['repos_url']
            instance = GithubOrgClient("google")
            self.assertEquals(instance.public_repos(), ["truth", "autoparse"])
            mock_repo.assert_called_once()
        mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, expected: bool) -> None:
        """ test method has_license"""
        self.assertEquals(GithubOrgClient.has_license(repo, license_key),
                          expected)


@parameterized_class([
    {
        'url_repos': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'names_repos': TEST_PAYLOAD[0][2],
        'license_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """implement classs"""
    @classmethod
    def setUpClass(cls):
        """setup class Test and start patcher"""
        urls_to_test = {
            'https://api.github.com/orgs/google': cls.url_repos,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def mock_request_get(url):
            """ sideeffect function to return Mock Object"""
            if url in urls_to_test:
                attrs = {'json.return_value': urls_to_test[url]}
                return Mock(**attrs)
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=mock_request_get)
        cls.get_patcher.start()

    def test_public_repos(self):
        """test method public_repos with fixtures"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.names_repos,
        )

    def test_public_repos_with_license_apache2(self):
        """test also has_licence used in public_repos method"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.license_repos,
        )

    @classmethod
    def tearDownClass(cls):
        """clear patcher"""
        cls.get_patcher.stop()
