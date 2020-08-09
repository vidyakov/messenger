"""Tests for server module"""


import unittest
from time import time

from server import get_message_to_user, process_client_message
from common.conf import (
    ACTION, TIME,
    RESPONSE, ERROR,
    TYPE, USER, ACCOUNT_NAME,
    ACCOUNT_STATUS, ERROR_400
)


class TestServer(unittest.TestCase):
    """Test case for server module"""
    time_for_testing = time()

    probe_msg = {
        ACTION: 'probe',
        TIME: time_for_testing,
        RESPONSE: 400,
        ERROR: None
    }

    true_presence_msg = {
        ACTION: 'presence',
        TIME: time_for_testing,
        TYPE: 'status',
        USER: {
            ACCOUNT_NAME: None,
            ACCOUNT_STATUS: None
        }
    }

    def test_good_response(self):
        """Test func get_message_to_user with good response"""
        result = get_message_to_user(400, None)
        result[TIME] = self.time_for_testing
        self.assertEqual(result, self.probe_msg)

    def test_valid_msg(self):
        """Test func process_client_message with valid message"""
        self.assertEqual(
            process_client_message(self.true_presence_msg),
            (200, None)
        )

    def test_process_client_message_without_time(self):
        """Test func process_client_message with invalid message"""
        for_test = self.true_presence_msg.copy()
        del for_test[TIME]
        self.assertEqual(
            process_client_message(for_test),
            (400, ERROR_400)
        )


if __name__ == '__main__':
    unittest.main()
