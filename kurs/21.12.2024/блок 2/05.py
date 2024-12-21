def f(a, b):
    if a == b:
        return 1
    elif int(a) < int(b):
        return 0
    x1 = bin(int(a, 2) - 1)[2:]
    x2 = a[0] + '0' * (len(a) - 1)
    if x2 != a:
        return f(x1, b) + f(x2, b)
    else:
        return f(x1, b)

print(f(a='1000000', b='1000'))
