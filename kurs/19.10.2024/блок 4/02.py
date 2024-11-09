import string
def to10(num, o):
    s = ''
    alph = string.digits + string.ascii_uppercase
    while num > 0:
        s += alph[num % o]
        num //= o
    return s[::-1]


s = 32 ** 30 + 8 ** 60 - 32
neu_s = to10(s, 4)

f = neu_s.count('3')
print(f)
