with open("24-1.txt") as f:
    s = f.read().strip()

max_length = 0  # Максимальная длина последовательности 'C'
current_length = 0  # Текущая длина последовательности 'C'

for char in s:
    if char == 'C':
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0  # Сбрасываем счётчик, если встретили другой символ

print(max_length)
