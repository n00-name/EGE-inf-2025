import string
# string.digits + string.ascii_uppercase
x = '0123456789ABCDE'
y = '0123456789ABCDEFG'

for i in x:
    for j in y:
        s1 = '123' + i + '5'
        s2 = '67' + j + '9'

        f = int(s1, 15) + int(s2, 17)
        if f % 131 == 0:
            print(f / 131)
            break
