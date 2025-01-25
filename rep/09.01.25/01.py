from functools import lru_cache


@lru_cache(maxsize=128, typed=False)
def f(n):
    if n % 2 == 0:
        return f(n // 2) + 5
    elif n % 2 != 0 and n % 5 == 0:
        return f(n // 5) + 2
    else:
        return 0



ans = set()

for i in range(1, 1_000_001):
    ans.add(f(i))
print(len(ans))