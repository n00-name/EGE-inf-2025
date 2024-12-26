def f(start, end):
    if start == end:
        return 1
    elif start < end:
        return 0
    else:
        return f(start - 1, end) + f(start - 2, end) + f(start // 3, end)


print(f(16, 11) * f(11, 6))
