def f(a, x, y):
    return (x * y < a) or (x < y) or (9 < x)

for a in range(0, 1000):
    if all(f(a, x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
        break
