"""Logger for server side of project"""

import logging.handlers
from os import path

from logs import FORMATTER, STREAM_HANDLER
from common.conf import LOGGING_LEVEL


SERVER_LOG_PATH = path.join(path.dirname(path.abspath(__file__)), 'server_logs', 'server.log')
SERVER_HANDLER = logging.handlers.TimedRotatingFileHandler(
    SERVER_LOG_PATH, interval=1, when='D', encoding='utf-8'
)
SERVER_HANDLER.setFormatter(FORMATTER)
SERVER_HANDLER.setLevel(logging.INFO)

SERVER_LOG = logging.getLogger('server')
SERVER_LOG.addHandler(SERVER_HANDLER)
SERVER_LOG.addHandler(STREAM_HANDLER)
SERVER_LOG.setLevel(LOGGING_LEVEL)
