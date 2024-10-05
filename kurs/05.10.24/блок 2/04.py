def f(a, x):
    return ((x % a == 0) <= ((x % 54 == 0) or (x % 130 == 0))) and (a > 110)


for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)
        break
