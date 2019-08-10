# Hacking With Monads:
# Functional Programming for the Blue Team
# A Def Con 27 Workshop August 10, 2019

# Demonstration of memoization technique
# using functools lru_cache

# Memoize code courtesy of
# Nabil Khaja, 2017
# https://medium.com/@nkhaja/memoization-and-decorators-with-python-32f607439f84

import sys
import functools
import time


@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n == 0:return 0
    if n == 1:return 1
    else: return fibonacci(n-1) + fibonacci(n-2)


start_time = time.perf_counter()

for i in range(0, 40):
    print(str(fibonacci(i)), end=" ")

end_time = time.perf_counter()

print("\nElapsed time for recursive memoized with lru_cache: " + str(end_time - start_time) + " seconds.")
