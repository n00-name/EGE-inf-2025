def f(a, x, y):
    return (x - y * 2 < a * 3) or (y * 2 > x) or (x * 3 > 50)

for a in range(1, 1000):
    if all(f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
