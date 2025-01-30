def f(x, y, a):
    return (4 * x + y < a) or (x < y) or (22 <= x)

for a in range(1, 1000):
    if all(f(x, y, a) for x in range(0, 1001) for y in range(0, 1001)):
        print(a)
        break
