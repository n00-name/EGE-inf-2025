def f(n):
    if n == 0:
        return 0
    elif n % 2 == 0:
        return f(n // 2) - 2
    else:
        return 2 + f(n - 1)

s = [str(f(i)) for i in range(0, 1000)]

print(s.count('-2'))
