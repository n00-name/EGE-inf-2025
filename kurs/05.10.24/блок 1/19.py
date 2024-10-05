def f(a, x, y):
    return (x * y < a * 4) or (x >= 21) or (x < y * 4)

for a in range(1, 1000):
    if all(f(a, x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
