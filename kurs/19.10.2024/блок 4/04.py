import string
def to10(num, o):
    s = ''
    alph = string.digits + string.ascii_uppercase
    while num > 0:
        s += alph[num % o]
        num //= o
    return s[::-1]


s = (2 * 343 ** 123 + 2401) * (3 * 343 ** 137 - 2401)
neu_s = to10(s, 7)
print(neu_s)
f = neu_s.count('6')
print(f)
