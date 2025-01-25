from itertools import product
count = 0
for i in product('A12345', repeat=6):
    s = ''.join(i)
    #print(s)

    nechet = ['A' if 'A' == _ else '1' if int(_) % 2 == 1 else '0' for _ in s]
    nechet = ''.join(nechet)
    #print(nechet)

    if nechet.count('A') == 1 and not('1A' in nechet or 'A1' in nechet):
        #print(s)
        print(nechet)
        count += 1

print(count)