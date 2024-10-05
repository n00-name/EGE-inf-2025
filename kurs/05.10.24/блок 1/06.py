def f(a, x):
    return (a % 3 == 0) and ((220 % x == 0) <= ((a % x != 0) <= (550 % x != 0)))

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)
        break
