import itertools

lst = []
with open('05.txt', 'r') as f:
    for line in f:
        lst.append(list(map(int, line.split())))

count = 0

# Для каждой тройки чисел
for triplet in lst:
    # Генерируем все возможные перестановки
    for perm in itertools.permutations(triplet):
        a, b, c = perm
        # Проверяем условие арифметической прогрессии
        if 2 * b == a + c:
            count += 1
            break  # Если хотя бы одна перестановка образует АП, прекращаем проверку для этой тройки

print(f"Количество троек, образующих арифметическую прогрессию: {count}")
