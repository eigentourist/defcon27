import sys
import os

from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator1 executing before function.')
        func(*args, **kwargs)
        print('decorator1 executing after function.')

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator2 executing before function.')
        func(*args, **kwargs)
        print('decorator2 executing after function.')

    return wrapper


def decorator3(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator3 executing before function.')
        func(*args, **kwargs)
        print('decorator3 executing after function.')

    return wrapper


@decorator1
@decorator2
@decorator3
def doWork(data):
    print(f"Working on {data}.")


doWork("this thing")
print("\n")
doWork("that thing")