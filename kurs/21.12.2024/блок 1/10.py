def f(start, end):
    if start == end:
        return 1
    elif start > end:
        return 0
    else:
        return f(start + 1, end) + f(int('2' + str(start)), end)


print(f(3, 678))
