def f(start, end):
    if start == end:
        return 1
    elif start < end:
        return 0
    else:
        return f(start - 2, end) + f(start // 2, end)

print(f(32, 14) * f(14, 1))
