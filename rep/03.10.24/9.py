with open('9.txt', 'r') as f:
    strings = f.read().splitlines()
# print(s)

count = 0
for string in strings:
    b = list(map(int, string.split()))
    b.sort()

    for i in b:
        if b.count(i) > 2:
            continue
    else:
        if len(set(b)) == 5 and b.count(min(b)) == 1:
            count += 1
            print(count, b)


print(count)