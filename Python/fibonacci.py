
# Fibonacci Sequence
# Iterative and Recursive Solutions
# Nabil Khaja, 2017
# https://medium.com/@nkhaja/memoization-and-decorators-with-python-32f607439f84

import sys
import time

# iterative
def fib_iterative(n):
      if (n == 0):
              return 0
      elif (n == 1):
              return 1
      elif (n >1 ):
              fn = 0
              fn1 = 1
              fn2 = 2
              for i in range(3, n):
                      fn = fn1+fn2
                      fn1 = fn2
                      fn2 = fn
              return fn


# Iterative Fibonacci version 2
# From https://www.bogotobogo.com/python/python_generators.php
def fib_iterative2(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


def fib_recursive(n):
    if n == 0:return 0
    if n == 1:return 1
    else: return fib_recursive(n-1) + fib_recursive(n-2)


start_time = time.perf_counter()

for i in range(0, 40):
    print(str(fib_iterative(i)), end=" ")

end_time = time.perf_counter()

print("\nElapsed time for iterative version 1: " + str(end_time - start_time) + " seconds.\n")


start_time = time.perf_counter()

for i in range(0, 40):
    print(str(fib_iterative2(i)), end=" ")

end_time = time.perf_counter()

print("\nElapsed time for iterative version 2: " + str(end_time - start_time) + " seconds.\n")


start_time = time.perf_counter()

for i in range(0, 40):
    print(str(fib_recursive(i)), end=" ")

end_time = time.perf_counter()

print("\nElapsed time for recursive version: " + str(end_time - start_time) + " seconds.")

