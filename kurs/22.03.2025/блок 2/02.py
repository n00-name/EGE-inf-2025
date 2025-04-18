with open("24-2.txt") as f:
    s = f.read().strip()  # Читаем строку из файла

max_length = 0  # Максимальная длина подходящей подстроки
current_length = 0  # Текущая длина подходящей подстроки

for char in s:
    if char not in "CF":  # Проверяем, что символ не C и не F
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0  # Обнуляем счётчик, если встретили C или F

print(max_length)
