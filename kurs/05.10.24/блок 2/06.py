def f(a, x):
    return (x & 19 == 0) and (x & 38 != 0) or ((x & 43 == 0) <= ((x & a == 0) and (x & 43 == 0)))

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)
        break
