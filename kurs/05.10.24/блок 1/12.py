def f(a, x):
    return ((x & 20 != 0) or (x & 55 != 0)) <= ((x & 7 == 0) <= (x & a != 0))

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)
        break
