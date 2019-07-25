import sys
import os


def decorator1(func):
    def wrapper():
        print('decorator1 executing before function.')
        func()
        print('decorator1 executing after function.')

    return wrapper


@decorator1
def doWork():
    print('Working.')


doWork()