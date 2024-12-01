def to4(x):
    s = ""
    while x > 0:
        s = str(x%4) + s
        x = x // 4
    return s
def f(n):
    s = to4(n)
    if n % 4 == 0:
        s = "20" + s + "1"
    else:
        s = s + to4((n%4)*5)
    return int(s, 4)

a = []
for n in range(1, 10000):
    if f(n) < 2407:
        a.append(n)
print(max(a))