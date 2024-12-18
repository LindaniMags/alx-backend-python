#!/usr/bin/env python3
"""
Parameterize a unit test
"""
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized

from utils import (
    access_nested_map
)


class TestAccessNestedMap(unittest.TestCase):
    """Tests for  access_nested_map function."""
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
        """Tests for access_nested_map outputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
