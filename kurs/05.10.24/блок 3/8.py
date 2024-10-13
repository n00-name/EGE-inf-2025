def f(a, x, y):
    return(2 * y + x != 70) or (x < y) or (a < x)

for a in range(0, 1000):
    if all(f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
