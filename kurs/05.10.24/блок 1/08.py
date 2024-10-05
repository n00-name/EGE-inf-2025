def f(a, x):
    return (x & 35 != 0) <= ((x & 31 == 0) <= (x & a != 0))

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)
        break
