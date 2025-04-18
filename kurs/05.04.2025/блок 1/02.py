# Чтение файла
with open("24-2.txt", "r") as file:
    text = file.read().strip()

max_seq = ""
current_seq = text[0]

for i in range(1, len(text)):
    if ord(text[i]) < ord(text[i - 1]):
        current_seq += text[i]
    else:
        if len(current_seq) > len(max_seq):
            max_seq = current_seq
        current_seq = text[i]

# Проверка последней последовательности
if len(current_seq) > len(max_seq):
    max_seq = current_seq

# Вывод результата
print(max_seq, len(max_seq))
