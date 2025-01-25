def f(x, a):
    return ((x % 9 == 0) <= (x % 6 != 0)) or (x + a >= 100)

for a in range(1, 100):
    if all(f(x, a) for x in range(1, 100)):
        print(a)
        break