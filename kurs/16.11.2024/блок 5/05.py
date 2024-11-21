from itertools import product

count = 0
for i in product(range(14), repeat=5):

    lst = [1 if x > 10 else 0 for x in i]

    if ''.join(map(str, i)).count('9') == 1 and sum(lst) <= 3 and i[0] != 0:
        count += 1
        print(i)
print(count)
