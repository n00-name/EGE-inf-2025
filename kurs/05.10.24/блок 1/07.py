def f(a, x):
    return (a % 12 == 0) and ((530 % x == 0) <= ((a % x != 0) <= (170 % x != 0)))

count = 0
for a in range(1, 1000):
    if all(f(a, x) for x in range(1, 1000)):
        count += 1
print(count)
