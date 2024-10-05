def f(a, x, y):
    return ((y - 20 < a) and (10 - x < a)) or (x * (y + 2) > 48)

for a in range(1, 1000):
    if all(f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
