def f(n):
    if n < 2:
        return n
    elif n >= 2 and n % 2 == 0:
        return f(n // 2) + 1
    elif n >= 2 and n % 2 == 1:
        return f(3 * n + 1) + 1

ans = 0
for n in range(1, 100_001):
    if f(n) == 16:
        ans += 1
print(ans)