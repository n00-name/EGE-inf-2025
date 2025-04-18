import string

x = string.digits + string.ascii_uppercase[:15]
print(x)

for i in x:
    s1 = f'A4{i}7F2'
    s2 = f'N{i}G5{i}H'
    s3 = f'74{i}M26'

    f = int(s1, 25) + int(s2, 25) + int(s3, 25)
    if f % 24 == 0:
        print(f / 24)