def f(a, x):
    return((x & 123 != 0) or (x & 98 != 0)) <= ((x & 75 == 0) <= (x & a != 0))

for a in range(0, 1000):
    if all(f(a, x) for x in range(0, 1000)):
        print(a)
        break
