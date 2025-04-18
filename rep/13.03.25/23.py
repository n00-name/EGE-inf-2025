def f(start, end):
    if start == end:
        return 1
    elif start > end or start == 60:
        return 0
    else:

        return f(start + 1, end) + f(start * 2, end) + f(start * 3, end)



def f1(start, end):
    if start == end:
        return 1
    elif start > end or start == 30:
        return 0
    else:

        return f1(start + 1, end) + f(start * 2, end) + f(start * 3, end)


print(f(10, 30) * f(30, 70) + f1(10, 60) * f(60, 70))
