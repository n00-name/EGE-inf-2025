def f(start, end):
    if start == end:
        return 1
    elif start < end or start == 28:
        return 0
    else:
        if start % 2 == 0:
            return f(start - 2, end) + f(start // 2, end)
        else:
            return f(start - 2, end) + f(start - 3, end)

print(f(98,1))