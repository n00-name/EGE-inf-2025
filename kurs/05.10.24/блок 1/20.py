def f(a, x, y):
    return (-2 * y + 3 * x < a) or (x > 20) or (y > 55)

for a in range(1, 1000):
    if all(f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
