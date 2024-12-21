def f(start, end):
    if start == end:
        return 1
    elif start > end or start == 25:
        return 0
    else:
        return f(start + 1, end) + f(start * 2 + 1, end)


print(f(1, 31))
