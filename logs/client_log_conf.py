"""Logger for client side of project"""

import logging.handlers
from os import path

from common.conf import LOGGING_LEVEL
from logs import FORMATTER, STREAM_HANDLER


CLIENT_LOG_PATH = path.join(path.dirname(path.abspath(__file__)), 'client_logs', 'client.log')
CLIENT_HANDLER = logging.FileHandler(CLIENT_LOG_PATH, encoding='utf-8')
CLIENT_HANDLER.setFormatter(FORMATTER)
CLIENT_HANDLER.setLevel(logging.INFO)

CLIENT_LOG = logging.getLogger('client')
CLIENT_LOG.addHandler(CLIENT_HANDLER)
CLIENT_LOG.addHandler(STREAM_HANDLER)
CLIENT_LOG.setLevel(LOGGING_LEVEL)
