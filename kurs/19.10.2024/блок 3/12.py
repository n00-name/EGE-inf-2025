import string
def to10(num, o):
    s = ''
    alph = string.digits + string.ascii_uppercase
    while num > 0:
        s += alph[num % o]
        num //= o
    return s[::-1]

for x in range(3001):
    s = 6 ** 260 + 6 ** 120 + 6 ** 60 - x
    neu_s = to10(s, 6)
    if neu_s.count('0') == 202:
        print(x)
        break
