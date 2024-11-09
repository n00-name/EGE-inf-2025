import string
def to10(num, o):
    s = ''
    alph = string.digits + string.ascii_uppercase
    while num > 0:
        s += alph[num % o]
        num //= o
    return s[::-1]


s = 4 ** 4 * 5 ** 69 - 70
neu_s = to10(s, 5)
print(neu_s)
print(neu_s.count('0'), neu_s.count('1'), neu_s.count('2'), neu_s.count('3'), neu_s.count('4'))
