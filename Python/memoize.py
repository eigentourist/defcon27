# Hacking With Monads:
# Functional Programming for the Blue Team
# A Def Con 27 Workshop August 10, 2019

# Demonstration of memoization technique

# Memoize code courtesy of
# Nabil Khaja, 2017
# https://medium.com/@nkhaja/memoization-and-decorators-with-python-32f607439f84

import sys
import functools
import time

def memoize(func):
    cache = func.cache = {}
    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memoized_func


@memoize
def fibonacci(n):
    if n == 0:return 0
    if n == 1:return 1
    else: return fibonacci(n-1) + fibonacci(n-2)


start_time = time.perf_counter()

for i in range(0, 40):
    print(str(fibonacci(i)), end=" ")

end_time = time.perf_counter()

print("\nElapsed time for memoized recursive version: " + str(end_time - start_time) + " seconds.")
