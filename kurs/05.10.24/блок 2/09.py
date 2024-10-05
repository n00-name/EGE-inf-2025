def f(a, x, y):
    return (2 * x + 3 * y != 72) or ((a > x) and (a > y))

for a in range(1, 1000):
    if all(f(a, x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
        break
