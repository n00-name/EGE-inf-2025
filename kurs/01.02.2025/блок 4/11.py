from functools import *
from sys import *
setrecursionlimit(10000)

@lru_cache(maxsize=1000)
def f(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return 3 + f(n//2 - 1)
    return 1


for i in range(1000):
    if f(i) == 19:
        print(i)
        break
