"""Utilities for project"""


import time
import json

from common.conf import (
    DEFAULT_PORT,
    DEFAULT_HOST,
    PORT_ARG,
    HOST_ARG,
    ENCODING,
    POCKET_SIZE
)


def get_current_host_and_port(argv):
    """ Return the default host and port or from command line parameters """
    host = argv[argv.index(HOST_ARG) + 1] if HOST_ARG in argv else DEFAULT_HOST
    port = int(argv[argv.index(PORT_ARG) + 1] if PORT_ARG in argv else DEFAULT_PORT)
    if not 1024 < port < 65535:
        raise ValueError
    return host, port


def get_time():
    """ Return current time """
    return time.time()


def send_message(sock, msg):
    """ Encode and send message """
    sock.send(json.dumps(msg).encode(ENCODING))


def receive_message(sock):
    """ Receive and decode message """
    return json.loads(sock.recv(POCKET_SIZE).decode(ENCODING))
