def f(a, x, y):
    return (y * 3 + x < a) or (x > 12) or (y > 15)

for a in range(1, 1000):
    if all(f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
