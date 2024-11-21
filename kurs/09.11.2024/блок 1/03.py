import string
x = string.digits + string.ascii_lowercase
for i in x:
    s1 = '8' + i + '121'
    s2 = '7' + i + '575'

    f = int(s1, 13) - int(s2, 13)
    if f % 19 == 0:
        print(f / 19, i)