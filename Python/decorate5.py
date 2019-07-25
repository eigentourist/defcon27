import sys
import os

from functools import wraps


def errorhandler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('errorhandler executing before function.')
        func(*args, **kwargs)
        print('errorhandler executing after function.')

    return wrapper


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('logger executing before function.')
        func(*args, **kwargs)
        print('logger executing after function.')

    return wrapper


def authenticator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('authenticator executing before function.')
        func(*args, **kwargs)
        print('authenticator executing after function.')

    return wrapper


@errorhandler
@logger
@authenticator
def doWork(data):
    print(f"Working on {data}.")


doWork("this thing")
print("\n")
doWork("that thing")