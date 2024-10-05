def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return (n - 1) * F(n - 1)
import sys
sys.setrecursionlimit(100000)


print((F(2024) + 2 * F(2023)) / F(2022))
