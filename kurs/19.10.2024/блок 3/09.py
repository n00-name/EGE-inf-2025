import string
x = string.digits + string.ascii_uppercase
for i in x:
    s1 = '131' + i + '1'
    s2 = '13' + i + '3'

    f = int(s1, 15) + int(s2, 17)
    if f % 11 == 0:
        print(f / 11)
