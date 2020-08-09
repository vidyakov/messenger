"""Server module"""


import sys
from socket import socket, AF_INET, SOCK_STREAM
import logging

from common.utils import (
    get_current_host_and_port,
    get_time,
    receive_message,
    send_message
)
from common.conf import (
    MAX_CONNECTIONS, PROBE_MSG,
    ACTION, TIME, USER,
    TYPE, RESPONSE, ERROR,
    ERROR_400
)
# This unused import only for logging.getLogger func
import logs.server_log_conf


LOG = logging.getLogger('server')


def get_message_to_user(response: int, error: str) -> dict:
    """Form probe message to user"""
    msg = PROBE_MSG.copy()
    msg[TIME] = get_time()
    msg[RESPONSE] = response
    msg[ERROR] = error

    if __debug__:
        LOG.debug(
            'Message to user: %(msg)s',
            {'msg': msg}
        )
    return msg


def process_client_message(msg: dict) -> (int, str or None):
    """Unpack user message"""
    if TIME in msg and ACTION in msg and USER in msg and TYPE in msg:
        LOG.info('Code 200 from message: %(msg)s', {'msg': msg})
        return 200, None

    LOG.error('Code 400 from message: %(msg)s', {'msg': msg})
    return 400, ERROR_400


def send_and_receive(sock: socket) -> None:
    """Receive presence message and send probe message"""
    client_sock, _ = sock.accept()  # _ = client_address
    from_user = receive_message(client_sock)
    if __debug__:
        LOG.debug(
            'Received message from user: %(msg)s',
            {'msg': from_user}
        )

    response, error = process_client_message(from_user)
    msg_to_user = get_message_to_user(response, error)
    send_message(client_sock, msg_to_user)
    if __debug__:
        LOG.debug('Message sent to user')

    client_sock.close()


def start_server() -> None:
    """Start server"""
    host, port = get_current_host_and_port(sys.argv)
    server_sock = socket(AF_INET, SOCK_STREAM)
    server_sock.bind((host, port))
    server_sock.listen(MAX_CONNECTIONS)
    LOG.info(
        'Starts on %(host)s:%(port)d',
        {'host': host, 'port': port}
    )

    try:
        while True:
            send_and_receive(server_sock)
    finally:
        server_sock.close()
        LOG.info('Closes')


if __name__ == '__main__':
    start_server()
