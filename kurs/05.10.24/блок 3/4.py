def f(a, x):
    return (a % 35 == 0) and ((730 % x == 0) <= ((a % x != 0) <= (110 % x != 0)))

count = 0
for a in range(1, 1001):
    if all(f(a, x) for x in range(1, 1000)):
        print(a)
        count += 1
print(count)
