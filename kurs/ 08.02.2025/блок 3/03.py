def f(x, y, a):
    return (x * y < 4 * a) or (x >= 21) or (x < 4 * y)

for a in range(-1000, 1000):
    if all(f(x, y, a) for x in range(1, 1001) for y in range(1, 1001)):
        print(a)
        break