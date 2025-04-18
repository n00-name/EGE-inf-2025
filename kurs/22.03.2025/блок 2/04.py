with open("24-4.txt") as f:
    lines = f.readlines()  # Читаем все строки файла

count = 0  # Счётчик строк, удовлетворяющих условию

for line in lines:
    if line.count('K') > line.count('U'):  # Сравниваем количество 'K' и 'U'
        count += 1

print(count)
