lst = []
with open('04.txt', 'r') as f:
    for line in f:
        lst.append(list(map(int, line.split())))

count = 0
for a, b, c in lst:
    # Вычисляем дискриминант
    D = b**2 - 4*a*c
    # Если D > 0, то уравнение имеет два действительных корня
    if D > 0:
        count += 1

print(count)
