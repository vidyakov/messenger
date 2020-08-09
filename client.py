"""Client module"""


from socket import socket, AF_INET, SOCK_STREAM
import sys
import logging

from common.utils import (
    get_current_host_and_port,
    get_time,
    send_message,
    receive_message
)
from common.conf import (
    PRESENCE_MSG, RESPONSE,
    ERROR, TIME
)
# This unused import only for logging.getLogger func
import logs.client_log_conf


LOG = logging.getLogger('client')


def get_presence_msg() -> dict:
    """ Form presence message to server """
    msg = PRESENCE_MSG.copy()
    msg[TIME] = get_time()
    if __debug__:
        LOG.debug(
            'Presence msg: %(msg)s',
            {'msg': msg}
        )
    return msg


def send_message_to_server(sock: socket) -> None:
    """ Send presence message to server """
    msg_to_server = get_presence_msg()
    send_message(sock, msg_to_server)
    if __debug__:
        LOG.debug(
            'Presence message had been sent %(msg)s',
            {'msg': msg_to_server}
        )


def receive_message_from_server(data: dict) -> int or (int, str):
    """ Receive probe message from server """
    if RESPONSE in data:
        if data[RESPONSE] == 200:
            LOG.info('Probe message have been received')
            return 200

    LOG.info('Code 400, error %(error)s', {'error': data[ERROR]})
    return 400, data[ERROR]


def start_client() -> None:
    """ Start client server """
    host, port = get_current_host_and_port(sys.argv)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    LOG.info(
        'Starts on %(host)s:%(port)d',
        {'host': host, 'port': port}
    )
    send_message_to_server(sock)
    data = receive_message(sock)
    receive_message_from_server(data)
    sock.close()
    LOG.info('Closes')


if __name__ == '__main__':
    start_client()
