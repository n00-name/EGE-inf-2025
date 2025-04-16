nmin = 100_000_000
summa = 0
def f(n):
    s = ''
    while n > 0:
        s = s + str(n % 5)
        n = n // 5
    return s[:1]


for n in range(1529, 9483):

    n_bin = bin(n)[-2:]
    if n_bin == '01' and f(n) == '3':
        summa += n
        nmin = min(nmin, n)

print(nmin, summa)
