def f(a, x):
    return((x & 26 != 0) or (x & 13 != 0)) <= ((x & 24 == 0) <= (x & a != 0))

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)
        break
