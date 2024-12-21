def f(start, end, count):
    if start == end and count == 6:
        return 1
    elif start > end or count > 6:
        return 0
    else:
        return f(start + 1, end, count + 1) + f(start + 2, end, count + 1) + f(start * 2, end, count + 1)

print(f(1, 20, 0))
