def f(a, x):
    return (x % 33 == 0) <= ((x % a != 0) <= (x % 242 != 0))

for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)
