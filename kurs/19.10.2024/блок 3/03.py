import string
def to10(num, o):
    s = ''
    alph = '0123456789' + string.ascii_lowercase
    while num > 0:
        s += alph[num % o]
        num //= o
    return s[::-1]
s = 5 * 6561 ** 46 + 5 * 729 ** 15 - 5 * 5832 - 5
neu_s = to10(s, 9)
print(neu_s.count('4'))
