def f(a, x):
    return (x & a != 0) <= (((x & 17 == 0) and (x & 5 == 0)) <= (x & 3 != 0))

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)

