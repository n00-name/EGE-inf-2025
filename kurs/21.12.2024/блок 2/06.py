def f(start, end, count, minn):
    if start == end:
        minn.add(count)
        return 1
    elif start > end:
        return 0
    else:
        return f(start + 1, end, count + 1, minn) + f(start + 2, end, count + 1, minn) + f(start * 2, end, count + 1, minn)

minn = set()
f(1, 28, 0, minn)
print(minn)



def f1(start, end, count):
    if start == end and count == 5:
        return 1
    elif start > end or count > 5:
        return 0
    else:
        return f1(start + 1, end, count + 1) + f1(start + 2, end, count + 1) + f1(start * 2, end, count + 1)


print(f1(1, 28, 0))
