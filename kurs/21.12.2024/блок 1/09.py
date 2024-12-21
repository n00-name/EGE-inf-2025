def f(start, end, count):
    if start == end and count <= 2:
        return 1
    elif start > end or count > 2:
        return 0
    else:
        return f(start + 1, end, count) + f(start * 2, end, count + 1) + f(start * 3, end, count + 1)


print(f(1, 100, 0))
