import string

x = string.digits + string.ascii_uppercase[:13]
print(x)

for i in x:
    s1 = f'1{i}1{i}1{i}1{i}1'
    s2 = f'20{i}24'
    s3 = f'1{i}235'

    f = int(s1, 23) + int(s2, 23) + int(s3, 23)
    if f % 22 == 0:
        print(f / 22)