import string
def to10(num, o):
    s = ''
    alph = '0123456789' + string.ascii_lowercase
    while num > 0:
        s += alph[num % o]
        num //= o
    return s[::-1]
s = 36 ** 11 + 6 ** 25 - 21
neu_s = to10(s, 6)
print(neu_s.count('5'))
