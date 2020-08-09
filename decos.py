"""Decorators for project
func log: first variant
class Log: second variant with option
"""


import os
import sys
import re
import logging
import inspect

# Only for func .getLogger
from logs import client_log_conf, server_log_conf


if re.search(r'client', os.path.split(sys.argv[0])[1]):
    print(sys.argv)
    LOG = logging.getLogger('client')
else:
    print(sys.argv)
    LOG = logging.getLogger('server')


def log(func):
    """This logger fixes func name, called, args and kwargs"""
    def inner(*args, **kwargs):
        log_string = 'Func: %(func)s Called: %(called)s Args: %(args)s Kwargs: %(kwargs)s'
        log_params = {
            'func': func.__name__,
            'called': inspect.stack()[1][3],
            'args': args,
            'kwargs': kwargs,
        }
        LOG.info(log_string, log_params)
        return func(*args, **kwargs)
    return inner


class Log:
    """
    This logger fixes func name, called, args and kwargs with option
    """
    def __init__(self, option):
        self.option = option

    def __call__(self, func):
        def inner(*args, **kwargs):
            log_string = 'Func: %(func)s Called: %(called)s Args: %(args)s Kwargs: %(kwargs)s'
            log_params = {
                'func': func.__name__,
                'called': inspect.stack()[1][3],
                'args': args,
                'kwargs': kwargs,
            }
            if self.option == 'info':
                LOG.info(log_string, log_params)
            else:
                LOG.debug(log_string, log_params)
            return func(*args, **kwargs)
        return inner
