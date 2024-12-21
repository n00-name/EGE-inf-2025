def f(start, end):
    if start == end:
        return 1
    elif start < end:
        return 0
    else:

        return f(start - 1, end) + f(start // 2, end)

print(f(30, 8) * f(8, 1))