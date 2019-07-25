import sys
import os


def decorator1(func):
    def wrapper():
        print('decorator1 executing before function.')
        func()
        print('decorator1 executing after function.')

    return wrapper


def doWork():
    print('Working.')


work = decorator1(doWork)
work()