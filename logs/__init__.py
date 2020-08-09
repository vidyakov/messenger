"""Logs packet"""

import logging


# Formatter for client and server logs
FORMATTER_STRING = '%(levelname)-10s%(asctime)-30s%(module)-10s%(message)s'
FORMATTER = logging.Formatter(FORMATTER_STRING)

# Stream handler for client and server logs
STREAM_HANDLER = logging.StreamHandler()
STREAM_HANDLER.setFormatter(FORMATTER)
STREAM_HANDLER.setLevel(logging.DEBUG)
