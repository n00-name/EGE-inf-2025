import re

# Читаем содержимое файла
with open("24-3.txt") as f:
    s = f.read().strip()

# Ищем все последовательности цифр в тексте
numbers = re.findall(r'\d+', s)

# Оставляем только нечётные числа и преобразуем их в int
odd_numbers = [int(num) for num in numbers if int(num) % 2 == 1]

# Находим максимальное нечётное число (если оно есть)
if odd_numbers:
    print(max(odd_numbers))
else:
    print("Нет нечётных чисел")
