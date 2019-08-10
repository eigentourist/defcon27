# Hacking With Monads:
# Functional Programming for the Blue Team
# A Def Con 27 Workshop August 10, 2019

# Decorator technique, manual implementation

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