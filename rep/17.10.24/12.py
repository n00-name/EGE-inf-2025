s = '>' + '2' * 20 + '3' * 100 + '5' * 117

while '>2' in s or '>3' in s or '>5' in s:
    if '>2' in s:
        s = s.replace('>2', '55>', 1)
    if '>3' in s:
        s = s.replace('>3', '333>', 1)
    if '>5' in s:
        s = s.replace('>5', '235>', 1)

s = s.replace('>', '')
print(s.count('2') * 2 + s.count('3') * 3 + s.count('5') * 5)