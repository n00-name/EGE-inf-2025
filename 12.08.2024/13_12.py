s = '1' * 70

while '1111' in s or '2222' in s:

    if '1111' in s:
        s = s.replace('1111', '22', 1)
    else:
        s = s.replace('2222', '11', 1)

print(s)  # 22
