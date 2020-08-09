"""Tests for client module"""


import unittest
from time import time

from client import get_presence_msg, receive_message_from_server
from common.conf import (
    TIME, ACTION,
    TYPE, USER,
    ACCOUNT_NAME,
    ACCOUNT_STATUS,
    RESPONSE, ERROR
)


class TestClient(unittest.TestCase):
    """Test case for client module"""
    time_for_test = time()

    response_200 = {
        ACTION: 'probe',
        TIME: time_for_test,
        RESPONSE: 200,
        ERROR: None
    }

    response_400 = {
        ACTION: 'probe',
        TIME: time_for_test,
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def test_presence_msg(self):
        """Test presence message"""
        presence = get_presence_msg()
        presence[TIME] = self.time_for_test
        self.assertEqual(presence, {
            ACTION: 'presence',
            TIME: self.time_for_test,
            TYPE: 'status',
            USER: {
                ACCOUNT_NAME: None,
                ACCOUNT_STATUS: None
            }
        })

    def test_response_from_server_200(self):
        """Test server response 200"""
        from_server = receive_message_from_server(self.response_200)
        self.assertEqual(from_server, 200)

    def test_response_from_server_400(self):
        """Test server response 400"""
        from_server = receive_message_from_server(self.response_400)
        self.assertEqual(
            from_server,
            (400, 'Bad Request')
        )


if __name__ == '__main__':
    unittest.main()
