def f(a, x):
    return (a < 50) and ((x % a != 0) <= ((x % 10 == 0) <= (x % 12 != 0)))

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)
