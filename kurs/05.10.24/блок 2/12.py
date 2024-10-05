def f(a, x, y):
    return (x * y < 2 * a) or (x >= 11) or (x < 2 * y)

for a in range(1, 1000):
    if all(f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
