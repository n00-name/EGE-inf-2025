def F(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2 and n % 4 == 0:
        return n - F(n // 4) - F(n - 4)
    elif n > 2 and n % 4 != 0:
        return 2 + F(n - 1) + F(n // 5)


count = 0
for i in range(40, 120 + 1):
    if 60 < F(i) <= 240:
        count += 1
print(count)