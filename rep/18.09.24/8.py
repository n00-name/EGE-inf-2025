from itertools import product

words = list(product('ЬРПЛЕА', repeat=5))

count = 0
ans = 0
for word in words:
    count += 1
    s = ''.join(word)
    print(count, s)

    if count <= 387:

        if word[-1] == 'Ь':

            ans += 1
print(ans)