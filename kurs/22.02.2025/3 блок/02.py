def f(x, y, a):
    return (75 != 2 * x + 3 * y) or (a > 3 * x) or (a > 2 * y)

for a in range(1, 1000):
    if all(f(x, y, a) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break