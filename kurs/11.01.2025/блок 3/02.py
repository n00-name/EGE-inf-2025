def f(x, y, a):
    return (5 * x + 3 * y != 60) or ((a > x) and (a > y))

for a in range(1, 1000):
    if all(f(x, y, a) for x in range(0, 500) for y in range(0, 500)):
        print(a)
        break