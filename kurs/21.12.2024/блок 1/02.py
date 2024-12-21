def func(start):
    if start % 10 == 9:
        return (start // 10 + 1) * 10 + start % 10
    return (start // 10 + 1) * 10 + (start % 10 + 1)


def f(start, end):
    if start == end:
        return 1
    elif start > end:
        return 0
    else:
        return f(start + 1, end) + f(func(start), end)


print(f(26, 49))
