import string
def to10(num, o):
    s = ''
    alph = '0123456789' + string.ascii_lowercase
    while num > 0:
        s += alph[num % o]
        num //= o
    return s[::-1]
s = 6 * 343 ** 5 + 5 * 49 ** 7 - 50
neu_s = to10(s, 7)
print(neu_s.count('6'))
