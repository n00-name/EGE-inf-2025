def f(a, x, y):
    return ((y - 40 < a) and (30 - y < a)) or (x * y > 20)

for a in range(1, 1000):
    if all(f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
