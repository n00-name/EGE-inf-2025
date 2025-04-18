import sys
sys.setrecursionlimit(100000)
def f(n):
    if n < 100:
        return 2 * n
    elif n > 99 and n % 2 == 0:
        return 0.5 * f(n - 1)
    elif n > 99 and n % 2 != 0:
        return 2 * f(n - 1)


print(1000 * f(16384) / f(7777))