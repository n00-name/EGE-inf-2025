def f(x, y, a):
    return (x + y <= 22) or (y <= x - 6) or (y >= a)

for a in range(0, 10000):
    if all(f(x, y, a) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)