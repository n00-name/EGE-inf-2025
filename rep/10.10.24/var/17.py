f = open("17.txt")
a = [int(s) for s in f]
mini = min(a)
par = []
for i in range(1, len(a)):
    if a[i] % 18 + a[i - 1] % 18 == mini:
        par.append(a[i] + a[i - 1])
print(len(par), max(par))