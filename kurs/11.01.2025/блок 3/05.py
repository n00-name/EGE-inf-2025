from itertools import permutations

count = 0
for i in permutations('ШАРЛАТАН'):
    s = ''.join(i)
    print(s)

    ifinglas = ['1' if _ in 'А' else '0' for _ in s]
    x = ''.join(ifinglas)
    if '11' in x or '00' in x:
        count += 1
        print(x)


print(count)
