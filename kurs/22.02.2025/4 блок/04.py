s = '>' + '1' * 25 + '2' * 17 + '3' * 10

while '>1' in s or '>2' in s or '>3' in s:

    if '>1' in s:
        s = s.replace('>1', '22>3')
    if '>2' in s:
        s = s.replace('>2', '2>')
    if '>3' in s:
        s = s.replace('>3', '11>2')

s = s[:-1]
print(s)
print(s.count('3') + s.count('2') + s.count('1'))