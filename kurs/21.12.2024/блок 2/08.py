def f(start, end):
    if start == end:
        return 1
    elif start > end:
        return 0
    else:
        return f(start + 2, end) + f(start + 5, end)


for i in range(100):
    if f(5, i) == 34:
        print(i)
