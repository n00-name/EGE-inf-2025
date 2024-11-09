import string
def to10(num, o):
    s = ''
    alph = string.digits + string.ascii_uppercase
    while num > 0:
        s += alph[num % o]
        num //= o
    return s[::-1]

for i in range(3001):
    s = 7 ** 100 - i
    neu_s = to10(s, 7)
    if neu_s.count('0') == 2:
        print(i)
