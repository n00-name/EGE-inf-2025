import string
def to10(num, o):
    s = ''
    alph = string.digits + string.ascii_uppercase
    while num > 0:
        s += alph[num % o]
        num //= o
    return s[::-1]


s = 36 ** 17 + 6 ** 48 - 17
neu_s = to10(s, 6)
print(neu_s.count('0'))
