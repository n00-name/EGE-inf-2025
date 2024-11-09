import string
def to10(num, o):
    s = ''
    alph = string.digits + string.ascii_uppercase
    while num > 0:
        s += alph[num % o]
        num //= o
    return s[::-1]

maxx = -1
for x in range(1, 2031):
    s = 6 ** 2030 + 6 ** 100 - x
    neu_s = to10(s, 6)

    f = neu_s.count('0')
    if f > 0:
        print(f)
        maxx = max(maxx, f)
print(maxx)
