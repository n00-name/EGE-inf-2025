from itertools import product
import string

# Генерация шестнадцатеричных цифр
s = string.digits + string.ascii_uppercase
s = s[:16]

count = 0
# Генерация всех перестановок длины 5
for i in product(s, repeat=5):
    # Проверяем, что числа в порядке неубывания
    if list(i) == sorted(i):
        count += 1

print(count)
