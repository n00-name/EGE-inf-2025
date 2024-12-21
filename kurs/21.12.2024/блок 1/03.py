def f(start, end):
    if start == end:
        return 1
    elif start > end or start == 8:
        return 0
    else:
        return f(start + 1, end) + f(start * 2, end)


print(f(2, 20) * f(20, 40))
