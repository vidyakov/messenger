"""Settings of project"""

import logging


DEFAULT_PORT = 8888
DEFAULT_HOST = 'localhost'

PORT_ARG = '-p'
HOST_ARG = '-h'

POCKET_SIZE = 4096
MAX_CONNECTIONS = 1
ENCODING = 'utf-8'

LOGGING_LEVEL = logging.DEBUG

ACTION = 'action'
TIME = 'time'
USER = 'user'
TYPE = 'type'
RESPONSE = 'response'
ERROR = 'error'
ACCOUNT_NAME = 'account_name'
ACCOUNT_STATUS = 'status'

# Never delete existing keys
PROBE_MSG = {
    ACTION: 'probe',
    TIME: None,
    RESPONSE: None,
    ERROR: None
}

# Never delete existing keys
PRESENCE_MSG = {
    ACTION: 'presence',
    TIME: None,
    TYPE: 'status',
    USER: {
        ACCOUNT_NAME: None,
        ACCOUNT_STATUS: None
    }
}

ERROR_400 = 'Bad Request'
