def f(a, x):
    return ((x & 13 != 0) and (x & 39 != 0)) <= ((x & a != 0) and (x & 13 != 0))

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)
        break
