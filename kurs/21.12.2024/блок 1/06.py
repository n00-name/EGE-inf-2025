def f(start, end):
    if start == end:
        return 1
    elif start > end or start == 8 or start == 15:
        return 0
    else:
        return f(start + 1, end) + f(start + 2, end) + f(start * 3, end)

print(f(3, 10) * f(10, 22))
