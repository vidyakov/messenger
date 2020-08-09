"""Tests for utilities"""


import unittest

from common.utils import get_current_host_and_port
from common.conf import (
    DEFAULT_HOST, DEFAULT_PORT,
    PORT_ARG, HOST_ARG
)


class TestUtils(unittest.TestCase):
    """Test Case for utilities"""
    test_port = 7777
    test_host = '127.0.0.1'

    def test_without_argv(self):
        """Test func get_current_host_and_port without arguments"""
        self.assertEqual(
            get_current_host_and_port([]),
            (DEFAULT_HOST, DEFAULT_PORT)
        )

    def test_with_argv(self):
        """Test func get_current_host_and_port with arguments"""
        self.assertEqual(
            get_current_host_and_port([PORT_ARG, self.test_port, HOST_ARG, self.test_host]),
            (self.test_host, self.test_port)
        )


if __name__ == '__main__':
    unittest.main()
