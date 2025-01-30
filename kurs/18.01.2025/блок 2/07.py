import sys
sys.setrecursionlimit(10**6)

def f(start, end):
    if start == end:
        return 1
    elif start > end:
        return 0
    else:

        return f(start + 3, end) + f(start * 4, end) + f(start * 5, end)

print(f(1, 5500))