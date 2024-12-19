import string

x = string.digits + string.ascii_uppercase[:1]
y = string.digits + string.ascii_uppercase[:1]
print(x)
print(y)

for x1 in x:
    for y1 in y:

        s1 = f'7{y1}23{x1}5'
        s2 = f'67{x1}9{y1}'
        s = int(s1, 25) + int(s2, 11)

        if s % 131 == 0:
            print(s/131)
            print(s1, s2)