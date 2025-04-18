import string

x = string.digits + string.ascii_uppercase[:9]
print(x)

for i in x:
    s1 = int(f'98{i}79641', 19)
    s2 = int(f'36{i}14', 19)
    s3 = int(f'73{i}4', 19)

    f = s1 + s2 + s3
    if f % 18 == 0:
        print(f / 18)