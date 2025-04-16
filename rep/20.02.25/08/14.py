import string

x = string.digits + string.ascii_uppercase[:9]

for i in x:
    f = int(f'3{i}2{i}1{i}0{i}1', 19) + int(f'{i}2024', 19) + int(f'1{i}077', 19)

    if f % 18 == 0:
        print(f / 18)