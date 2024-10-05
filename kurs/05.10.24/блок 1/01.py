def f(a, x):
    return ((x % a == 0) and (x % 21 == 0)) <= (x % 18 == 0)

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)
        break
