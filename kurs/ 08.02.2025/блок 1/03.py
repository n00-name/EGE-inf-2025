lst = []
with open('03.txt', 'r') as f:
    for line in f:
        lst.append(list(map(int, line.split())))

count = 0
for a, b, c in lst:
    # Сортируем числа, чтобы гарантировать правильный порядок (гипотенуза будет максимальным числом)
    a, b, c = sorted([a, b, c])

    # Проверяем условие Пифагора: a^2 + b^2 == c^2
    if a ** 2 + b ** 2 == c ** 2:
        count += 1

print(count)
