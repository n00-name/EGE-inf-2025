import re

# Открываем файл и читаем содержимое
with open("24-1.txt", "r") as file:
    text = file.read()

# Находим все последовательности цифр, ограниченные нецифровыми символами или началом/концом строки
numbers = re.findall(r'(?<!\d)\d+(?!\d)', text)

# Фильтруем только чётные числа и преобразуем их в int
even_numbers = [int(num) for num in numbers if num[-1] in '02468']

# Если чётные числа найдены, выводим максимальное
if even_numbers:
    print(max(even_numbers))
else:
    print("Чётных чисел не найдено")
