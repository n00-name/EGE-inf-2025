import sys
sys.setrecursionlimit(100000)

def f(n):
    if n > 3000:
        return n
    else:
        return f(n + 2) + 2


print(f(40) - f(43))
