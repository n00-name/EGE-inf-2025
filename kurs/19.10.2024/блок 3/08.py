import string
x = string.digits + string.ascii_uppercase
for i in x:
    s1 = '66' + i + '63'
    s2 = '5' + i + '810'

    f = int(s1, 17) - int(s2, 17)
    if f % 11 == 0:
        print(f / 11)
        break
