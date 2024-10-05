def f(a, x, y):
    return ((x - 20 < a) and (10 - y < a)) or (y * (x + 4) > 45)

for a in range(1, 1000):
    if all(f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
