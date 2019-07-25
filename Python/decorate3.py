import sys
import os


def decorator1(func):
    def wrapper(*args, **kwargs):
        print('decorator1 executing before function.')
        func(*args, **kwargs)
        print('decorator1 executing after function.')

    return wrapper


@decorator1
def doWork(data):
    print(f"Working on {data}.")


doWork("this thing")
doWork("that thing")