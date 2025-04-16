def f(n):
    s = []
    while n > 0:
        s.append(n % 12)
        n //= 12
    return s

s = 12 ** 34 + 7 * 12 ** 26 - 3 * 12 ** 5 + 552

print(len(f(s)))