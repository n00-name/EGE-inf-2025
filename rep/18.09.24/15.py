def f(a, x):
    return (a + x < 123) <= ((x % 5 == 0) <= (x % 7 != 0))

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)
        break

