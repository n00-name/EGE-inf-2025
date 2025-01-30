def f(start, end):
    if start == end:
        return 1
    elif start > end or start == 17 or start == 11:
        return 0
    else:

        return f(start + 1, end) + f(start + 4, end) + f(start * 2, end)


print(f(3, 24) )
