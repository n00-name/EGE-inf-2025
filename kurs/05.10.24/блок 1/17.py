def f(a, x, y):
    return (y * 3 + x * 2 != 130) or (x * 3 > a) or (y * 2 > a)

for a in range(1, 1000):
    if all(f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
