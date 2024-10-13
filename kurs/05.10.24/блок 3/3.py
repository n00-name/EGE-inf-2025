def f(a, x, y):
    return (x % a == 0) <= ((x % a == 0) <= (x % 34 == 0) and (x % 51 == 0))

for a in range(1, 1000):
    if all(f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
