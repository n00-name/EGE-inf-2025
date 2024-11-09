import string
x = string.digits + string.ascii_uppercase
for i in x:
    s1 = '123' + i + '5'
    s2 = '1' + i + '233'

    f = int(s1, 15) + int(s2, 15)
    if f % 14 == 0:
        print(f / 14)