def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + F(n - 1)
    elif n > 1 and n % 2 == 1:
        return F(n - 1) + 2 * F(n - 2)


print(F(19)) # ans 49197
