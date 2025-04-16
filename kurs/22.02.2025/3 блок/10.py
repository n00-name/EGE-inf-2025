import sys
sys.setrecursionlimit(100000)

def f(n):
    if n == 1:
        return 1
    else:
        return (n + 1) * f(n - 1)

print((f(2024) + 3 * f(2023)) / f(2022))